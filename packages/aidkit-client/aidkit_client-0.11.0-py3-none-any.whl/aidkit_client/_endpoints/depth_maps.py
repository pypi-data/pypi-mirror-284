from io import BytesIO
from typing import BinaryIO, List

import numpy as np
from PIL import Image

from aidkit_client._endpoints.models import DepthMapResponse
from aidkit_client.aidkit_api import HTTPService
from aidkit_client.exceptions import ResourceWithIdNotFoundError

SAVING_TYPE = np.uint16
DEPTH_MAP_RESOLUTION_KEY = "DepthMapResolution"


def deserialize(content: bytes) -> List[List[float]]:
    image = Image.open(BytesIO(content))
    data = np.asarray(image, dtype=SAVING_TYPE)
    metadata = image.text  # type:ignore[attr-defined]
    resolution = float(metadata[DEPTH_MAP_RESOLUTION_KEY])
    return (data * resolution).tolist()


class DepthMapAPI:
    api: HTTPService

    def __init__(self, api: HTTPService):
        self.api = api

    async def create(
        self,
        file: BinaryIO,
        resolution: float,
        observation_id: int,
    ) -> DepthMapResponse:
        return DepthMapResponse(
            **(
                await self.api.post_multipart_data(
                    path=f"/observation/{observation_id}/depth_map",
                    files={
                        "depth_map_data": (
                            f"depth_map_{observation_id}",
                            file,
                        )
                    },
                    data={"resolution": resolution},
                )
            ).body_dict_or_error(f"Failed to create depth map for observation {observation_id}.")
        )

    async def get_by_observation_id(self, observation_id: int) -> DepthMapResponse:
        result = await self.api.get(path=f"observation/{observation_id}/depth_map", parameters=None)
        if result.is_not_found:
            raise ResourceWithIdNotFoundError(
                f"Depth map for observation with id {observation_id} not found"
            )
        return DepthMapResponse(
            **result.body_dict_or_error(
                f"Error fetching depth map for observation with id {observation_id}."
            )
        )
