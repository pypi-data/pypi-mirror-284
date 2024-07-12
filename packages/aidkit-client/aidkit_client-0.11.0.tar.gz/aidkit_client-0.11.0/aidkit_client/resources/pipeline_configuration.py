from pathlib import Path
from typing import Any, Dict, List

from pydantic import BaseModel
from yaml import Dumper, dump, safe_load

from aidkit_client.resources.augmentation import Augmentation


class PipelineConfiguration(BaseModel):
    """
    Configuration object for a complete pipeline, consisting of multiple augmentations.

    :param name: The name of the pipeline.
    :param augmentations: A list of augmentation objects, each defining a step in the pipeline.
    """

    name: str
    augmentations: List[Augmentation]


def import_pipeline_configuration_from_yaml(
    path_to_yaml_file: Path,
) -> PipelineConfiguration:
    """
    Imports a pipeline configuration from a YAML file.
    WARNING: The file format for the YAML file may be subject to change between aidkit versions.

    :param path_to_yaml_file: The file path to the YAML file containing the pipeline configuration.
    :return: A PipelineConfiguration object populated with the data from the YAML file.
    """
    file_content = _read_from_file(path_to_yaml_file)
    parsed_file_content = safe_load(file_content)
    return _dictionary_to_pipeline_configuration(parsed_file_content)


def export_pipeline_configuration_to_yaml(
    pipeline_configuration: PipelineConfiguration,
    file_path: Path,
) -> None:
    """
    Exports a PipelineConfiguration object to a YAML file.
    WARNING: The file format for the YAML file is not explicitly defined or versioned.

    :param pipeline_configuration: The pipeline configuration to be exported.
    :param file_path: The file path where the YAML file should be saved.
    """
    file_content = _dictionary_to_yaml_formatted_string(data=pipeline_configuration.dict())
    _write_to_file(file_path, file_content)


Dictionary = Dict[Any, Any]


def _dictionary_to_yaml_formatted_string(data: Dictionary) -> str:
    return dump(
        data,
        sort_keys=False,
        Dumper=Dumper,
    )


def _dictionary_to_pipeline_configuration(data: Dictionary) -> PipelineConfiguration:
    return PipelineConfiguration(
        name=data["name"],
        augmentations=[
            Augmentation(name=each["name"], parameters=each["parameters"])
            for each in data["augmentations"]
        ],
    )


FileContent = str


def _parse_yaml_file_content(file_content: FileContent) -> Dictionary:
    return safe_load(file_content)


def _read_from_file(file_path: Path) -> FileContent:
    with open(file_path, "r") as reader:
        return reader.read()


def _write_to_file(file_path: Path, file_content: FileContent) -> None:
    with open(file_path, "w") as writer:
        writer.write(file_content)
