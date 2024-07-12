import json
import uuid
from io import BytesIO
from typing import Any, Dict, Optional

from PIL.Image import Image
from PIL.Image import open as open_image

from aidkit_client._endpoints.constants import Constants
from aidkit_client._endpoints.models import (
    ListAugmentationResponse,
    ParameterSpecsResponse,
)
from aidkit_client.aidkit_api import HTTPService


class AugmentationsAPI:
    api: HTTPService

    def __init__(self, api: HTTPService):
        self.api = api

    async def list_available_augmentations(self) -> ListAugmentationResponse:
        list_augmentation_response = await self.api.get(
            path=Constants.AUGMENTATIONS_PATH, parameters=None
        )

        return ListAugmentationResponse(
            **list_augmentation_response.body_dict_or_error(
                "Error getting the list of available augmentations."
            )
        )

    async def get_augmentation_parameters(self, augmentation_name: str) -> ParameterSpecsResponse:
        return ParameterSpecsResponse(
            **(
                await self.api.get(
                    path=f"{Constants.AUGMENTATIONS_PATH}/{augmentation_name}/parameters",
                )
            ).body_dict_or_error(f"Failed to get parameters for: '{augmentation_name}'")
        )

    async def augment_single_image(
        self,
        augmentation_method: str,
        augmentation_parameters: Dict[str, Any],
        image: Image,
        segmentation_map: Image,
        depth_map: Image,
        depth_map_resolution: float,
        random_seed: Optional[float] = None,
    ) -> Image:
        image_bytes = BytesIO()
        image.save(image_bytes, format="PNG")

        observation_name = str(uuid.uuid4())

        seg_map_bytes = BytesIO()
        segmentation_map.save(seg_map_bytes, format="PNG")

        depth_map_bytes = BytesIO()
        depth_map.save(depth_map_bytes, format="PNG")

        data = {
            "augmentation_name": augmentation_method,
            "parameters": json.dumps(augmentation_parameters),
            "depth_map_resolution": depth_map_resolution,
        }

        files = {
            "image": (
                observation_name + ".png",
                image_bytes.getvalue(),
                "image/png",
                {"Expires": "0"},
            ),
            "segmentation_map": (
                observation_name + "_seg.png",
                seg_map_bytes.getvalue(),
                "image/png",
                {"Expires": "0"},
            ),
            "depth_map": (
                observation_name + "_depth.png",
                depth_map_bytes.getvalue(),
                "image/png",
                {"Expires": "0"},
            ),
        }

        if random_seed:
            data["random_seed"] = (None, str(random_seed))

        augmented_image_response = await self.api.post_multipart_data(
            path=Constants.AUGMENTATIONS_PATH, data=data, files=files
        )

        augmented_image_bytes = augmented_image_response.body_bytes_or_error(
            "Error while augmenting an image."
        )

        return open_image(BytesIO(augmented_image_bytes), formats=["PNG"])
