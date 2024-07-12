"""
Custom errors for the aidkit python client.
"""


class AidkitClientError(Exception):
    """
    Base Error for all errors explicitely raised from the aidkit client.
    """


class ResourceWithIdNotFoundError(Exception):
    """
    No resource with the passed ID was found.
    """


class ResourceWithNameNotFoundError(Exception):
    """
    No resource with the passed name was found.
    """


class MultipleSubsetsReportAggregationError(Exception):
    """
    The report requests tries to aggregate data from pipeline runs on multiple
    subsets.
    """


class AidkitClientNotConfiguredError(AidkitClientError):
    """
    The client is used before being configured.
    """


class RunTimeoutError(AidkitClientError):
    """
    A pipeline run took too long to finish.
    """


class TargetClassNotPassedError(AidkitClientError):
    """
    No target class was passed when trying to run a pipeline which requires a
    target class.
    """


class PipelineRunError(AidkitClientError):
    """
    A pipeline run did not finish successfully, but was stopped or failed.
    """


class AuthenticationError(AidkitClientError):
    """
    The user is not authenticated properly.
    """

    def __init__(self, *args: object) -> None:
        """
        Create a new error with the appropriate error message.

        :param args: Context for the error.
        """
        super().__init__(
            *args,
            "For instructions on how to configure authentication, consult the documentation.",
        )


class AugmentationNotFoundError(Exception):
    """
    The augmentation requested does not exist.
    """


class AugmentationExecutionError(Exception):
    """
    The augmentation execution has failed.
    """


class AugmentationAlgorithmicError(Exception):
    """
    A runtime error that occurs during the execution of an augmentation.
    Examples are mathematical errors (e.g., division by zero), non-convergence
    when solving optimization problems, and other issues that occur for some
    input data (e.g., non-existing classes in a segmentation map).
    """


class TooManyRequestsError(Exception):
    """
    The client has sent too many requests to the endpoint.
    """


class DataFormatError(ValueError):
    """
    The file is corrupt or non-parsable.
    """


class DataDimensionError(ValueError):
    """
    The depth-map, segmentation-map and/or Image are the incorrect dimensions.
    """


class InvalidParametersError(ValueError):
    """
    There is an issue with the provided parameters.
    """

    def __init__(self, server_error_msg: str) -> None:
        super().__init__(server_error_msg)
        self.message = server_error_msg

    def __str__(self) -> str:
        """
        Print string of invalid parameters message.

        :return: A string containing the error message.
        """
        return f"Parameters invalid: {self.message}"
