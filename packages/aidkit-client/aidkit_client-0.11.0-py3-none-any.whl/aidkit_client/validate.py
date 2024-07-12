from pathlib import Path
from typing import Union

import numpy as np
from numpy.typing import NDArray
from PIL import UnidentifiedImageError
from PIL.Image import Image as PILImage
from PIL.Image import open as open_image

from aidkit_client.exceptions import DataDimensionError, DataFormatError


def _validate_image_format(image: Union[PILImage, Path]) -> None:
    """
    Validate format of PNG image.

    :param image: PNG image or its path.
    :return: None.
    :raises DataFormatError: If fails to open the image or the image has other format than PNG.
    :raises TypeError: If the type of the image is neither PIL.Image nor pathlib.Path.
    """
    if isinstance(image, Path):
        try:
            open_image(image, formats=("png",))
        except (UnidentifiedImageError, ValueError, TypeError) as error:
            raise DataFormatError(
                f"Error opening the image file at path '{image}'. "
                f"The image might be corrupted or have the wrong format. "
                f"Please ensure that the file is a valid PNG image. "
            ) from error
    elif isinstance(image, PILImage):
        if (format := image.format) != "PNG":
            raise DataFormatError(
                f"The image must have PNG format, but it has {format} format instead. "
            )
    else:
        raise TypeError(
            f"The image must be of type `PIL.Image` or `pathlib.Path`, "
            f"but it is of type {type(image).__name__} instead. "
        )


def _validate_image_content(image: Union[PILImage, Path]) -> NDArray:
    """
    Validate content of PNG image.

    :param image: PNG image or its path.
    :return: image content as NDArray.
    :raises DataFormatError: If the image content has values outside the range [0, 1].
    """
    binary = image if isinstance(image, PILImage) else open_image(image, formats=("png",))
    content = np.asarray(binary)
    if content.min() < 0 or content.max() > 255:
        raise DataFormatError("The content of the image must be within the range [0, 255]. ")

    return content / np.iinfo(np.uint8).max


def _validate_image_dimensions(image: Union[PILImage, Path]) -> None:
    """
    Validate image dimensions.

    :param image: PNG image or its path.
    :return: None.
    :raises DataDimensionError: If number of image dimensions or channels is wrong.
    """
    content = _validate_image_content(image)
    if (ndim := content.ndim) != 3:
        raise DataDimensionError(f"The image must have 3 dimensions, but it has {ndim} instead. ")
    if (shape := content.shape[2]) != 3:
        raise DataDimensionError(f"The image must have 3 channels, but it has {shape} instead. ")


def validate_image(image: Union[PILImage, Path]) -> None:
    """
    Validate PNG image.

    :param image: PNG image or its path.
    :return: None.
    :raises DataFormatError: If the image is corrupted, has a wrong format, or if its content is
        outside the range [0, 1].
    :raises DataDimensionError: If the image has the wrong number of dimensions or channels.

    """
    _validate_image_format(image)
    _validate_image_dimensions(image)
    _validate_image_content(image)


def validate_map(image: Union[PILImage, Path]) -> None:
    """
    Validate segmentation/depth map dimensions.

    :param image: Segmentation or depth map.
    :return: None.
    :raises DataDimensionError: If number of dimensions is wrong.
    """
    _validate_image_format(image)

    binary = image if isinstance(image, PILImage) else open_image(image, formats=("png",))
    content = np.asarray(binary)
    if (ndim := content.ndim) != 2:
        raise DataDimensionError(f"The map must have 2 dimensions, but it has {ndim} instead. ")
