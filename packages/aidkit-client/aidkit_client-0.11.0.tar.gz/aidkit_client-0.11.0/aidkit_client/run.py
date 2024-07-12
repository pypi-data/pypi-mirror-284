import asyncio
import hashlib
import json
import logging
import os
import pprint
import random
import threading
import time
import typing
from collections import Counter
from datetime import datetime
from enum import Enum, auto
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
from IPython import get_ipython  # type: ignore
from IPython.display import clear_output, display  # type: ignore
from PIL.Image import Image
from tenacity import RetryCallState, retry, retry_if_exception_type, stop_after_attempt

from aidkit_client.exceptions import TooManyRequestsError
from aidkit_client.resources.augmentation import Augmentation

LOG = logging.getLogger(__name__)


class JobState(Enum):
    """
    States of the lifecycle of an augmentation job.

    CREATED -> PENDING -> RUNNING -> RETRY -> COMPLETED|FAILED|CANCELLED|RETRY_EXCEEDED
    """

    CREATED = auto()
    PENDING = auto()
    RUNNING = auto()
    RETRY = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    FAILED = auto()
    RETRY_EXCEEDED = auto()


# @dataclass
class AugmentationJob:
    """
    A job definition that contains all information to execute a single augmentation on an image.
    An AugmentationJob is stateful and will transition through different lifecycle stages.
    """

    _id_counter: int = 0
    _thread_lock = threading.Lock()

    def __init__(
        self,
        augmentation: Augmentation,
        image: Path,
        segmentation_map: Path,
        depth_map: Path,
        depth_map_resolution: float,
    ):
        """
        Initializes an Augmentation Job.

        :param augmentation: the augmentation that is executed in this job
        :param image: the image to augment
        :param segmentation_map: the segmentation map that belongs to the image
        :param depth_map: the depth map that belongs to the image
        :param depth_map_resolution: the resolution of the depth_map
        """
        self.augmentation = augmentation
        self.image = image
        self.segmentation_map = segmentation_map
        self.depth_map = depth_map
        self.depth_map_resolution = depth_map_resolution

        with AugmentationJob._thread_lock:
            AugmentationJob._id_counter += 1
            self._job_id = AugmentationJob._id_counter
        self._output_path: Optional[Path] = None
        self._random_seed: Optional[int] = random.randint(a=0, b=1_000_000)  # noqa: S311
        self._state: JobState = JobState.CREATED

        self._job_completed_time: Optional[float] = None
        self._job_completed_timestamp: Optional[float] = None
        self._exception: Optional[Exception] = None

    @property
    def output_path(self) -> Optional[Path]:
        """
        The output path where the job will save the augmentation result.

        :return: The output path where the jobs saves the result.
        """
        return self._output_path

    @output_path.setter
    def output_path(self, output_path: Path) -> None:
        self._output_path = output_path

    @property
    def random_seed(self) -> Optional[int]:
        """
        The random seed to use with the augmentation.

        It is initialized to a random value when creating the AugmentationJob.
        To control the randomness in the augmentation, set `random_seed` to an explicit value.

        :return: the random seed of the job.
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed: int) -> None:
        self._random_seed = random_seed

    @property
    def state(self) -> JobState:
        """
        The state of the job in the lifecycle.

        :return: the current state of the job. Returns COMPLETED if the file in the `output_path` exists.
        """
        if self.output_path and self.output_path.exists():
            return JobState.COMPLETED
        return self._state

    @staticmethod
    def _retry_callback(retry_state: RetryCallState) -> None:
        job = retry_state.args[0]
        job._state = JobState.RETRY
        LOG.debug(
            f"Job {job._job_id} transitioned to state {job.state}. This is Retry attempt #{retry_state.attempt_number}."
        )

    @staticmethod
    def _retry_error_callback(retry_state: RetryCallState) -> None:
        job = retry_state.args[0]
        job._state = JobState.RETRY_EXCEEDED
        LOG.info(
            f"Job {job._job_id} transitioned to state {job.state}. It failed after {retry_state.attempt_number} retry attempts."
        )
        augmentation_description = {
            "name": job.augmentation.name,
            "parameters": job.augmentation.parameters,
        }
        pp = pprint.PrettyPrinter(indent=2, sort_dicts=False)
        LOG.debug(f"\n{pp.pformat(augmentation_description)}")

    @retry(
        retry=retry_if_exception_type(TooManyRequestsError),
        reraise=True,
        stop=stop_after_attempt(10),
        after=_retry_callback,
        retry_error_callback=_retry_error_callback,
    )
    async def _run_augmentation(self) -> Image:
        try:
            self._state = JobState.RUNNING
            LOG.debug(f"Job {self._job_id} transitioned to state {self._state}.")

            result = await self.augmentation.augment(
                self.image, self.segmentation_map, self.depth_map, self.depth_map_resolution
            )

            if self.output_path:
                result.save(self.output_path)

            self._state = JobState.COMPLETED
            LOG.debug(f"Job {self._job_id} transitioned to state {self._state}.")
        except TooManyRequestsError as tmre:
            LOG.debug(f"Job {self._job_id}: server responded with '{tmre}'")
            await asyncio.sleep(1)
            raise
        except asyncio.CancelledError:
            self._state = JobState.CANCELLED
            LOG.debug(f"Job {self._job_id} is cancelled and transitioned to state {self._state}.")
            raise
        except Exception as e:
            self._state = JobState.FAILED
            self._exception = e
            LOG.info(
                f"Job {self._job_id} ran into an error: {e} and transitioned to state {self._state}.\n"
                f"ERROR >> {e}"
            )
            raise
        return result

    async def run(self) -> Image:
        """
        Runs the augmentation job and returns the augmented image.

        :return: the augmented image
        """
        return await self._run()

    async def _run(self, semaphore: Optional[asyncio.Semaphore] = None) -> Image:
        self._state = JobState.PENDING

        if not semaphore:
            semaphore = asyncio.Semaphore()

        async with semaphore:
            job_start_time = time.time()

            result = await self._run_augmentation()

            job_end_time = time.time()
            self._job_completed_time = job_end_time - job_start_time
            self._job_completed_timestamp = job_end_time

        return result


class RunException(Exception):
    """
    An exception that occurs when managing AugmentationRun states.
    """

    pass


class AugmentationRun:
    """
    An augmentation run manages a collection of augmentation jobs.

    It schedules and runs augmentation jobs concurrently and non-blocking.
    This means that a caller that creates and runs an `AugmentationRun` can
    continue to interact with it, e.g., by checking the status of the jobs or
    to obtain intermediate results.

    A typical workflow is to instantiate an AugmentationRun, then call `start`,
    observe the progress through `job_states` and `runtime_statistics (or by using
    `track_progress` in an interactive jupyter notebook).
    The augmentation run can be interrupted with `interrupt` and continued
    later by calling `start` again.
    """

    def __init__(self, augmentation_jobs: List[AugmentationJob]) -> None:
        """
        Instantiates an AugmentationRun.

        :param augmentation_jobs: a list of augmentation jobs the AugmentationRun manages.
        """
        self.jobs = augmentation_jobs

        self._run_futures: List[asyncio.Future] = []
        self._threads: List[threading.Thread] = []

    def job_states(self) -> typing.Counter[JobState]:
        """
        Summarizes the state of the managed jobs.

        :return: A counter of number of jobs per state.
        """
        stats: typing.Counter[JobState] = Counter()
        for job in self.jobs:
            stats[job._state] += 1
        return stats

    def get_jobs_with_exception(
        self,
    ) -> List[Tuple[AugmentationJob, JobState, Exception]]:
        """
        Retrieve jobs and their error message that failed because of an exception.

        :return: A tuple of (reference to the augmentation job, the job state, the exception)
        """
        return [(job, job.state, job._exception) for job in self.jobs if job._exception]

    def runtime_statistics(self) -> Dict:
        """
        Summarizes runtime statistics of completed augmentation jobs.

        :return: a dict with runtime statistics with keys
            `mean_last_minute`: the mean roundtrip time of requests completed in the last minute
            (including retries)
            `current_fpm`: the number of requests completed in the last minute

        """
        completed_timestamps = [
            job._job_completed_timestamp
            for job in self.jobs
            if job._job_completed_timestamp and job._state == JobState.COMPLETED
        ]
        times_last_minute = [
            job._job_completed_time
            for job in self.jobs
            if job._job_completed_timestamp
            and job._state == JobState.COMPLETED
            and job._job_completed_timestamp > (time.time() - 60)
        ]
        current_fpm = [
            completed_ts
            for completed_ts in completed_timestamps
            if completed_ts > (time.time() - 60)
        ]

        if current_fpm and times_last_minute:
            return {
                "mean_last_minute": np.mean(np.array(times_last_minute)),
                "current_fpm": len(current_fpm),
            }
        else:
            return {}

    def is_running(self) -> bool:
        """
        An augmentation run can be in state "running" or "not running".

        If the augmentation run is "running", task workers are working through the list of
        augmentation jobs to execute them.

        :return: true, if workers are active to run augmentation jobs.
        """
        if self._run_futures:
            return not all(run_future.done() for run_future in self._run_futures)
        else:
            return False

    async def _execute_chunk_in_thread(
        self, chunk: List[AugmentationJob], max_concurrent: int = 10
    ) -> None:
        try:
            loop = asyncio.get_running_loop()
            LOG.debug(
                f"Executing chunk of size: {len(chunk)} in thread {threading.get_native_id()} with event loop {id(loop)}."
            )
            semaphore = asyncio.Semaphore(max_concurrent)

            coros = [job._run(semaphore) for job in chunk]

            run_future = asyncio.gather(*coros, return_exceptions=True)
            self._run_futures.append(run_future)

            await run_future
        except asyncio.CancelledError:
            LOG.debug(f"Cancelled all jobs handled by worker thread {threading.get_native_id()}.")

    async def start(self, max_concurrent: int = 5, max_threading: int = 1) -> None:
        """
        Starts or restarts an augmentation run for all augmentation jobs that are not yet completed.

        The started augmentation run creates multiple worker threads that each runs multiple
        concurrent asynchronous requests to the augmentation service.
        The `start` spins up the workers in the background and returns once the they are started.

        The request pressure on the augmentation service is controlled by setting
        `max_concurrent` and `max_threading`. The total number of requests that are processed in parallel is the
        product of both values. Setting good values depends on the data, augmentation and server configuration.
        A good rule of thumb is to first increase the value of `max_concurrent` until there is no further increase
        in the frames per minute (see `runtime_statistics` to track the statistics).
        Then increase the number of threads.

        :param max_concurrent: the number of concurrent async request jobs per thread.
        :param max_threading: the number of threads to start.
        :raises RunException: an AugmentationRun can only be started once and raises an exception if
            `start` is called on an AugmentationRun that is already running.
        """
        if self.is_running():
            raise RunException(
                "Run in progress. You need to call `interrupt` to interrupt the"
                "current run before you can start a new one."
            )

        unfinished_jobs: List[AugmentationJob] = [
            job for job in self.jobs if job._state != JobState.COMPLETED
        ]

        # reset job state and tracking information
        for job in unfinished_jobs:
            job._state = JobState.CREATED
            job._exception = None
            job._job_completed_time = None
            job._job_completed_timestamp = None

        LOG.info(f"Starting run for {len(unfinished_jobs)} jobs.")
        _threads = []
        self._run_futures = []

        for chunk in np.array_split(np.array(unfinished_jobs), max_threading):
            thread = threading.Thread(
                target=asyncio.run,
                args=(
                    self._execute_chunk_in_thread(chunk.tolist(), max_concurrent=max_concurrent),
                ),
            )

            _threads.append(thread)
            thread.start()
            LOG.debug(f"Started worker thread with id={thread.ident}.")
        LOG.info(f"Started {len(_threads)} worker threads.")
        self._threads = _threads

    async def interrupt(self) -> None:
        """
        Interrupts an augmentation run.

        The `interrupt` sends cancel requests to all workers.
        Cancelled jobs will be re-executed when restarting the augmentation run.
        """
        for run_future in self._run_futures:
            run_future.cancel()

        LOG.info("Interrupting augmentation run. This can take a few seconds...")

        while self.is_running():
            LOG.debug("Waiting until all scheduled coroutines ar cancelled.")
            await asyncio.sleep(1)

        LOG.info("Augmentation run is interrupted.")

    async def track_progress(self, interval: int = 1) -> None:
        """
        Displays the current job state counts and runtime information.

        Note: this function can only be called from an IPython environment.

        :param interval: the update frequency in seconds
        :raises RunException: if the function is called from a non-IPython environment.
        """
        ip = get_ipython()
        if ip is not None:
            try:
                while True:
                    clear_output(wait=True)
                    timings = self.runtime_statistics()
                    status = self.job_states()

                    display(status)
                    if timings:
                        display(
                            f"Average roundtrip time single frame (including retries): {timings['mean_last_minute']:.2f} sec"
                        )
                        display(f"Frames per Minute: {timings['current_fpm']}")
                    if not self.is_running():
                        break
                    await asyncio.sleep(interval)
            except asyncio.CancelledError:
                return
        else:
            raise RunException("`track progress` can only be executed from an IPython environment.")


def augment_single(job: AugmentationJob) -> Image:
    """
    Runs a single augmentation job.

    :param job: the augmentation job to run.
    :return: the augmented image.
    """
    return asyncio.run(job._run())


def _hash_augmentation_parameters(augmentation: Augmentation) -> str:
    parameters = augmentation.parameters
    hash_ = hashlib.md5(json.dumps(parameters, sort_keys=True).encode("utf-8")).hexdigest()
    return hash_


def augment_multiple(
    jobs: List[AugmentationJob], root_output_path: Optional[Path] = None
) -> AugmentationRun:
    """
    Creates an AugmentationRun that will store the augmentation results into
    a specified output path.

    The results of an augmentation job are saved using the following file name pattern:
    `augmentation_<hash>/image_filename_<random-seed>.png`
    where `<hash>` is a unique hash based on the augmentation parameters.

    Each augmentation directory also contains a yaml file that contains the
    parameter specification of the augmentation.

    Jobs where the output path already exists are set to COMPLETED. This allows to pick up
    an unfinished run at a later point in time.

    :param jobs: the augmentation jobs to include in the augmentation run.
    :param root_output_path: The root path for the augmentation run to save the results.
    :return: the created augmentation run.
    """
    if root_output_path is None:
        ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        root_output_path = Path("augmentation_runs") / Path(f"run_{ts}")

    path_creation_counter = 0
    for job in jobs:
        output_path = Path(
            root_output_path,
            Path(
                f"{job.augmentation.name}_{_hash_augmentation_parameters(job.augmentation)[0:12]}"
            ),
            Path(f"{job.image.stem}_{job.random_seed}.png"),
        )

        job.output_path = output_path

        # Consider jobs that have an output as completed
        if output_path.exists():
            LOG.debug(f"Found output file for job {job._job_id}. Setting status to completed.")
            job._state = JobState.COMPLETED
        else:
            job._state = JobState.CREATED

        if not output_path.parent.exists():
            path_creation_counter += 1
            output_path.parent.mkdir(parents=True)

        config_yaml = output_path.parent / Path("config.yaml")

        if not config_yaml.exists():
            with open(config_yaml, "w") as file:
                file.write(job.augmentation.to_yaml())

    augmentation_run = AugmentationRun(augmentation_jobs=jobs)
    already_completed = augmentation_run.job_states()[JobState.COMPLETED]
    if already_completed == len(jobs):
        LOG.warn(
            """All of the jobs are already completed. If you want to re-run the jobs, 
            choose a different output path or delete existing files."""
        )
    else:
        total_number_of_directories = len(set(os.listdir(root_output_path)))
        LOG.info(
            f"Finished creating the output paths for a total of {len(jobs)} augmentation jobs.\n"
            f">> The root of the output is '{root_output_path}'.\n"
            f">> There are {path_creation_counter} newly created output directories (one for each augmentation).\n"
            f">> In total, there are now {total_number_of_directories} output directories.\n"
            f">> Out of the {len(jobs)} jobs, there are already {already_completed} completed. These will be skipped by the augmentation run."
        )

    return AugmentationRun(augmentation_jobs=jobs)
