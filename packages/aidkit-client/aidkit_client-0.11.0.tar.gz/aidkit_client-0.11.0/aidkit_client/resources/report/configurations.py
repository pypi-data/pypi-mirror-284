from dataclasses import dataclass
from typing import Any, Dict, List, Union

MethodName = str
ConfigurationName = str
MethodConfigurationParameterString = str


@dataclass(frozen=True)
class Range:
    """
    Represents a numerical range with a minimum and maximum value.

    This class is immutable.

    :param min: The minimum value of the range.
    :param max: The maximum value of the range.
    """

    min: float
    max: float

    def __str__(self) -> str:
        """
        Provide a string representation of the Range instance.

        :return: A string in the format "min: [min value], max: [max value]", with values formatted to two decimal places.
        """
        return f"min: {self.min:.2f}, max: {self.max:.2f}"


@dataclass(frozen=True)
class VaryingParameterInfo:
    """
    Encapsulates information about a varying parameter, which can either be a numeric range or a list of categorical options.

    This class supports parameters that can either vary continuously within a range or discretely among a set of options.

    :param parameter_info: The varying parameter information, either as a Range or a list of categorical strings.
    """

    parameter_info: Union[Range, List[str]]

    def __str__(self) -> str:
        """
        Provide a string representation of the VaryingParameterInfo instance.

        If the parameter_info is a Range, it returns the string representation of Range.
        If it is a list of strings, it returns a comma-separated string of the options.

        :return: A string representation of the parameter information.
        """
        if isinstance(self.parameter_info, Range):
            return str(self.parameter_info)

        return ", ".join(self.parameter_info)


@dataclass(frozen=True)
class MethodConfiguration:
    """
    Information about a particular augmentation method configuration. This includes the parameters
    that remain fixed for the method, the number of augmentations per frames produced by this method
    as well as the ranges for the varying method parameters.
    """

    parameters: Dict[str, Any]
    augmentations_per_frame: int
    varying_parameters_info: Dict[str, VaryingParameterInfo]


@dataclass(frozen=True)
class ReportConfiguration:
    """
    Configuration parameters and general information about the report retrieved.
    """

    pipeline_run_ids: List[int]
    dataset_name: str
    subset_name: str
    number_of_frames: int
    odd_tags: Dict[int, List[str]]
    method_configurations: Dict[MethodName, Dict[ConfigurationName, MethodConfiguration]]
    method_configuration_names: Dict[
        MethodName, Dict[MethodConfigurationParameterString, ConfigurationName]
    ]

    def get_number_of_augmented_frames(self) -> int:
        """
        Get the total number of augmented frames in the pipeline. The total number of augmented
        frames is the number of original frames times the number of augmentations per frame.
        :return: Total number of augmented frames.
        """
        total_number_of_augmentations_per_frame = 0
        for configuration in self.method_configurations.values():
            for parameter in configuration.values():
                total_number_of_augmentations_per_frame += parameter.augmentations_per_frame
        return self.number_of_frames * total_number_of_augmentations_per_frame
