import asyncio
import os
import random
import uuid
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Type, Union

import ruamel.yaml as rt_yaml  # type : ignore
import yaml
from bs4 import BeautifulSoup
from jsonschema import Draft4Validator, validators
from PIL.Image import Image
from PIL.Image import open as open_image
from pydantic import BaseModel
from rich.console import Console
from rich.table import Table
from tabulate import tabulate

from aidkit_client._endpoints.augmentations import AugmentationsAPI
from aidkit_client.configuration import get_api_client
from aidkit_client.exceptions import (
    DataDimensionError,
    DataFormatError,
    InvalidParametersError,
)

ParameterName = str
ParameterValue = Any


class Augmentation(BaseModel):
    """
    Interface to the Augmentation Service.
    """

    name: str
    parameters: Dict[str, Any]

    @staticmethod
    def from_yaml(name: str, path: Path) -> "Augmentation":
        """
        Instantiate an augmentation of type provided in the `name` parameter with parameters read
        from the yaml file located at `path`.

        :param name: Name of the augmentation to instantiate.
        :param path: Path to the yaml file specifying the parameters for the augmentation.
        :return: An augmentation of type `name` with parameters read from `path`.
        """
        with open(path) as file:
            parameters = yaml.safe_load(file)

        return Augmentation(name=name, parameters=parameters)

    def to_yaml(self) -> str:
        """
        Return the parameters of the augmentation as a yaml string.

        :return: Parameters of the augmentation as a yaml string.
        """
        return yaml.safe_dump(self.parameters)

    async def augment_batch(
        self,
        input_paths: List[Tuple[Path, Path, Path]],
        target_path: Path,
        depth_map_resolution: float,
        random_seed: Union[int, List[int], None],
    ) -> List[Union[Path, BaseException]]:
        """
        Augment multiple images with the augmentation method.

        :param input_paths: List of three-tuples of paths specifying image and map data. Where Tuple[0] is
            the image file path, Tuple[1] is the segmentation map file path, and Tuple[2] is the
            depth map file path.
        :param target_path: File path specifying the directory where the resulting augmented images will be saved.
        :param depth_map_resolution: Resolution of the depth map in meters. For example, if a pixel
            value of `1` in the depth map corresponds to a distance of 3cm, `depth_map_resolution`
            is `0.03`.
        :param random_seed: Set a single random seed which can be used to reproduce the entire batch of images or provide
            a list of random seeds for each image in the batch.
        :raises DataDimensionError: If the dimensions or number of channels of the image, segmentation map
            or depth map are incorrect.
        :raises DataFormatError: If the image, segmentation map or depth map are not of type PIL.Image or
            cannot be loaded from the given path.
        :return: List of file paths of the augmented images.
        """
        if len(input_paths) == 0:
            raise DataFormatError("The list of file paths provided is empty.")
        seeds: Union[List[int], List[None]] = []

        if isinstance(random_seed, int):
            random.seed(random_seed)
            seeds = [
                int(random.random())  # noqa: S311
                for _ in range(len(input_paths))
            ]
        elif isinstance(random_seed, list):
            if len(input_paths) != len(random_seed):
                raise DataFormatError(
                    "The list of random seeds is not the same length as the number of input images."
                )

            seeds = random_seed

        async def augmentation_task(
            image: Image,
            segmentation_map: Image,
            depth_map: Image,
            random_seed: Optional[int] = None,
        ) -> Path:
            result = await self.augment(
                image=image,
                segmentation_map=segmentation_map,
                depth_map=depth_map,
                depth_map_resolution=depth_map_resolution,
                random_seed=random_seed,
            )
            filename = f"{uuid.uuid4()}.png"
            if not os.path.exists(target_path):
                os.makedirs(target_path)
            image_path = target_path / Path(filename)
            result.save(image_path)
            return image_path

        tasks = [
            augmentation_task(
                image=open_image(image_path),
                segmentation_map=open_image(seg_map_path),
                depth_map=open_image(depth_map_path),
                random_seed=seed,
            )
            for (image_path, seg_map_path, depth_map_path), seed in zip(
                input_paths, seeds if seeds else [None] * len(input_paths)
            )
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

    async def augment(
        self,
        image: Union[Image, Path],
        segmentation_map: Union[Image, Path],
        depth_map: Union[Image, Path],
        depth_map_resolution: float,
        random_seed: Optional[int] = None,
    ) -> Image:
        """
        Augment a single image using the augmentation method.

        :param image: Image to augment as a PIL Image or path to the image.
        :param segmentation_map: Segmentation map as a PIL Image or path to the segmentation map.
        :param depth_map: Depth map as a PIL Image or path to the depth map.
        :param depth_map_resolution: Resolution of the depth map in meters. For example, if a pixel
            value of `1` in the depth map corresponds to a distance of 3cm, `depth_map_resolution`
            is `0.03`.
        :param random_seed: Random seed for reproducibility.
        :raises DataDimensionError: If the dimensions or number of channels of the image, segmentation map
            or depth map are incorrect.
        :raises DataFormatError: If the image, segmentation map or depth map are not of type PIL.Image or
            cannot be loaded from the given path.
        :return: The result of applying the augmentation to the image.
        """
        image, segmentation_map, depth_map = self._validate_input_images(
            image, segmentation_map, depth_map
        )

        api_service = get_api_client()
        augmented_image = await AugmentationsAPI(api=api_service).augment_single_image(
            augmentation_method=self.name,
            augmentation_parameters=self.parameters,
            image=image,
            segmentation_map=segmentation_map,
            depth_map=depth_map,
            depth_map_resolution=depth_map_resolution,
            random_seed=random_seed,
        )

        return augmented_image

    @staticmethod
    def _validate_input_images(
        image: Union[Image, Path],
        segmentation_map: Union[Image, Path],
        depth_map: Union[Image, Path],
    ) -> Tuple[Image, Image, Image]:
        image = open_image(image) if isinstance(image, Path) else image
        segmentation_map = (
            open_image(segmentation_map) if isinstance(segmentation_map, Path) else segmentation_map
        )
        depth_map = open_image(depth_map) if isinstance(depth_map, Path) else depth_map

        names = ["Depth map", "Segmentation map", "Image"]
        for img in zip(names, [depth_map, segmentation_map, image]):
            try:
                assert isinstance(img[1], Image)
            except AssertionError as error:
                raise DataFormatError(
                    f"{img[0]} is not of type 'PIL.Image' or a correct file path. "
                    f"You can test if your image, segmentation map or depth map is valid "
                    f"using functions `validate_image` or `validate_map` from "
                    f"`aidkit_client.validate` module respectively. "
                ) from error

        img_channels = len(image.getbands())
        seg_map_channels = len(segmentation_map.getbands())
        depth_map_channels = len(depth_map.getbands())

        if img_channels != 3:
            raise DataDimensionError(
                f"The image provided should have 3 channels it has {img_channels}. "
                f"You can test if your image is valid using function "
                f"`validate_image` from `aidkit_client.validate` module. "
            )
        if seg_map_channels != 1:
            raise DataDimensionError(
                f"The segmentation map provided should have 1 channel it has {seg_map_channels}. "
                f"You can test if your segmentation map is valid using function "
                f"`validate_map` from `aidkit_client.validate` module. "
            )
        if depth_map_channels != 1:
            raise DataDimensionError(
                f"The depth map provided should have 1 channel it has {depth_map_channels}. "
                f"You can test if your depth map is valid using function "
                f"`validate_map` from `aidkit_client.validate` module. "
            )

        if not image.size == segmentation_map.size == depth_map.size:
            raise DataDimensionError(
                f"The image, segmentation map, and depth map must have the same "
                f"heights and widths but image has {image.size}, segmentation "
                f"map has {segmentation_map.size}, and depth map has "
                f"{depth_map.size}."
            )

        return image, segmentation_map, depth_map


@dataclass
class AugmentationParameterSpecification:
    """
    An interface for handling augmentation parameters.
    """

    _schema: Dict[str, Any]

    @property
    def schema(self) -> Dict[str, Any]:
        """
        Get the JSON schema of the augmentation paramater specification as a python `dict`.

        :return: A dictionary of the Augmentation Parameter schema.
        """
        return self._schema

    @classmethod
    async def get(cls, augmentation_name: str) -> "AugmentationParameterSpecification":
        """
        Get the parameter specification of an Augmentation.

        :param augmentation_name: The name of the augmentation to get parameters for.
        :return: The augmentation parameter specification.
        """
        api_service = get_api_client()
        response = await AugmentationsAPI(api_service).get_augmentation_parameters(
            augmentation_name=augmentation_name
        )
        return AugmentationParameterSpecification(_schema=response.specs)

    def _build_table(self, as_html: bool = False) -> Union[str, Table]:
        """
        Generate table representation of Augmentation Parameters.

        :param as_html: Flag if the table should be returned in HTML format.
        :return: Tabulate table of augmentation parameters.
        """
        properties = self._schema.get("properties")

        def resolve_ref(ref: Dict, schema: Dict) -> Dict:
            if "$ref" in ref:
                ref_path = ref["$ref"].split("/")[1:]
                resolved_ref = schema
                for key in ref_path:
                    resolved_ref = resolved_ref[key]
                return resolve_ref(resolved_ref, schema)
            else:
                return ref

        headers = ["parameter", "key", "type", "default", "description"]
        values = []

        def recursive_properties(
            properties: Any, parent_key: Optional[str] = None
        ) -> List[List[Any]]:
            if isinstance(properties, dict):
                for key, value in properties.items():
                    if isinstance(value, dict):
                        key_path = f"{parent_key}.{key}" if parent_key else key
                        _type = value.get("type")
                        default = value.get("default")
                        title = value.get("title")
                        description = value.get("description")
                        values.append([title, key_path, _type, default, description])
                        all_of_content = value.get("allOf")
                        if (
                            isinstance(all_of_content, list)
                            and len(all_of_content) == 1
                            and isinstance(all_of_content[0], dict)
                        ):
                            ref = value["allOf"][0]
                            resolved_ref = resolve_ref(ref, self._schema)
                            recursive_properties(
                                resolved_ref.get("properties"), parent_key=key_path
                            )
            return values

        if as_html:
            html_str = tabulate(recursive_properties(properties), headers=headers, tablefmt="html")
            html_table: BeautifulSoup = BeautifulSoup(html_str, "html.parser")
            for cell in html_table.find_all(["th", "td"]):
                if "style" in cell.attrs:
                    cell["style"] += " text-align: left; vertical-align: top;"
                else:
                    cell["style"] = "text-align: left; vertical-align: top;"
            return str(html_table)
        else:
            table: Table = Table(title="Augmentation Parameters")
            for header in headers:
                table.add_column(header)
            table_rows = recursive_properties(properties)
            for row in table_rows:
                item_strs = [str(item) for item in row]
                table.add_row(*item_strs)
            return table

    def _parse_schema_with_defaults(
        self, include_description: bool = False
    ) -> Dict[str, Union[Any, Dict[str, Any]]]:
        """
        Get the parameters of the augmentation as a dictionary with default values where they exit.
        Other parameters have the value `None` set and this needs to be replaced by an actual
        valid parameter value before using the augmentation.

        :param include_description: If true, the dictionary returned includes a description and the
            type of each field where this information is available.
        :return: A dictionary with default parameters.
        """

        def extend_with_default(
            validator_class: Type[Draft4Validator],
        ) -> Type[Draft4Validator]:
            def set_defaults(
                validator: Draft4Validator,
                properties: Dict,
                instance: Dict,
                schema: Dict,
            ) -> None:
                for property_, subschema in properties.items():
                    entry = {}
                    entry["default"] = (
                        subschema["default"]
                        if "default" in subschema and not isinstance(instance, list)
                        else None
                    )
                    entry["description"] = (
                        subschema["description"] if "description" in subschema else None
                    )

                    entry["type"] = subschema["type"] if "type" in subschema else None

                    if include_description:
                        instance.setdefault(property_, entry)
                    else:
                        instance.setdefault(property_, entry["default"])

            return validators.extend(
                validator_class,
                {"properties": set_defaults},
            )

        FillDefaultValidatingDraft4Validator = extend_with_default(Draft4Validator)
        parameters_dictionary: Dict[str, Any] = {}
        FillDefaultValidatingDraft4Validator(self._schema).validate(parameters_dictionary)

        return parameters_dictionary

    def default_dict(self) -> Dict[str, Any]:
        """
        Create a set of example parameter values for the augmentation.

        The example will include default values of the augmentation method if they exist. However, some parameters
        have no default values (e.g., class index mappings). The example will leave these fields
        empty, and the values must be manually added to make the parameter configuration valid.

        :return: A dictionary with default parameters.
        """
        parsed_schema = self._parse_schema_with_defaults()
        return parsed_schema

    def default_yaml(self, include_description: bool = True) -> str:
        """
        Get the parameters of the augmentation as a yaml string with default values where they exist.

        Other parameters will have no value set and a valid parameter needs to be specified manually
        before using the augmentation.

        :param include_description: Add a description to each field as a comment in the yaml file.
        :return: A string representation of the example yaml configuration.
        """
        default_parameters = self._parse_schema_with_defaults()
        yaml_parameters = yaml.safe_dump(default_parameters)
        yaml_parser = rt_yaml.YAML()
        parsed_yaml_parameters = yaml_parser.load(yaml_parameters)

        if include_description:
            parameters_with_descriptions = self._parse_schema_with_defaults(
                include_description=True
            )

            max_length = 0
            for line in yaml_parameters.split("\n"):
                max_length = len(line) if len(line) > max_length else max_length

            for (
                parameter_name,
                parameter_values,
            ) in parameters_with_descriptions.items():
                if "description" in parameter_values:
                    parsed_yaml_parameters.yaml_add_eol_comment(
                        parameter_values["description"],
                        parameter_name,
                        column=max_length + 1,
                    )

        string_stream = StringIO()
        yaml_parser.dump(parsed_yaml_parameters, string_stream)
        output_str = string_stream.getvalue()
        string_stream.close()

        return output_str

    def as_table(self) -> None:
        """
        Print to console the parameters in a table format.
        """
        table = self._build_table()
        console = Console()
        console.print(table)

    def _repr_html_(self) -> str:
        """
        HTML table representation of parameters.

        :return: HTML table representation of augmentation parameters.
        """
        table: str = self._build_table(as_html=True)  # type: ignore[assignment]
        return table


@dataclass
class AvailableAugmentations:
    """
    Interface for currently available augmentations.
    """

    _available_augmentations: Dict[str, AugmentationParameterSpecification]

    @classmethod
    async def get(cls) -> "AvailableAugmentations":
        """
        Get the list of available augmentation methods.

        :return: An `AvailableAugmentations` object holding the list of augmentation methods that
            can be used.
        """
        api_service = get_api_client()
        augmentation_methods = await AugmentationsAPI(
            api=api_service
        ).list_available_augmentations()

        available_augmentations = {
            augmentation_name: AugmentationParameterSpecification(augmentation_specs.specs)
            for augmentation_name, augmentation_specs in augmentation_methods.augmentations.items()
        }

        return AvailableAugmentations(available_augmentations)

    @property
    def augmentation_names(self) -> List[str]:
        """
        Available augmentation method names as a list of strings.

        :return: List of strings containing the available augmentation names.
        """
        return list(self._available_augmentations.keys())

    def augmentation_parameter_specification(
        self, augmentation_name: str
    ) -> AugmentationParameterSpecification:
        """
        Get the parameter specification of an Augmentation.

        :param augmentation_name: The name of the augmentation to get parameters for.
        :return: The augmentations parameter specification.
        """
        return self._available_augmentations[augmentation_name]

    def get_augmentation(
        self, name: str, parameters: Optional[Dict[str, Any]] = None
    ) -> Augmentation:
        """
        Instantiate an augmentation of the specified type, if it is available, with the given parameters.

        :param name: Name of the augmentation to create.
        :param parameters: Parameters of the augmentation.
        :raises KeyError: If the name provided does not match the name of an available augmentation.
        :raises InvalidParametersError: If at least one of the parameters provided is not valid for
            the selected augmentation.
        :return: An augmentation of type `name` with parameters specified by `parameters`.
        """
        if name not in self.augmentation_names:
            raise KeyError(
                f"The augmentation method '{name}' is not available. Possible values are "
                f"{self.augmentation_names}."
            )

        if not parameters:
            return Augmentation(name=name, parameters={})

        method_parameters = self.augmentation_parameter_specification(name).default_dict()
        invalid_parameters = list()
        for parameter in parameters.keys():
            if parameter not in method_parameters:
                invalid_parameters.append(parameter)

        if invalid_parameters:
            invalid_parameters_string = ", ".join(invalid_parameters)
            raise InvalidParametersError(
                "At least one of the provided parameters is not valid for the augmentation "
                f"'{name}'. The invalid parameters are: '{invalid_parameters_string}'. To get a "
                f"list of available parameters for the augmentation '{name}', use "
                "`AvailableAugmentations.augmentation_parameter_specification(augmentation_name="
                f"'{name}')`."
            )

        return Augmentation(name=name, parameters=parameters)

    def __repr__(self) -> str:
        """
        Return the string representation of the list of augmentation method names.

        :return: A string containing all the method names separated by a line return.
        """
        augmentation_list = "\n".join(self.augmentation_names)
        return f"Available augmentations:\n\n{augmentation_list}"
