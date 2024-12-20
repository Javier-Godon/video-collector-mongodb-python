from fastapi import APIRouter

from src.usecases.get_video_list.get_video_list_handler import get_video_list
from src.usecases.get_video_list.get_video_list_query import GetVideoListQuery
from src.usecases.get_video_list.rest.get_video_list_request import GetVideoListRequest
from src.usecases.get_video_list.rest.video_detail_response import VideoDetailResponse

router = APIRouter()


@router.post("/collector/videos/", response_model=list[VideoDetailResponse])
async def get_video_list_filtered(request: GetVideoListRequest):
    query = from_request_to_query_video_list(request)
    result = await get_video_list(query)
    return await from_bson_list_to_video_detail_response_list(result)


def from_request_to_query_video_list(request: GetVideoListRequest) -> GetVideoListQuery:
    return GetVideoListQuery(
        sha_id=request.sha_id,
        element_alias=request.element_alias,
        unix_epoch_start=request.unix_epoch_start,
        unix_epoch_end=request.unix_epoch_end
    )


async def from_bson_list_to_video_detail_response_list(bson_list: list) -> list[VideoDetailResponse]:
    response = []
    for element in bson_list:
        video_detail = VideoDetailResponse(
            uuid=element['uuid'],
            element_alias=element['element_alias'],
            unix_epoch_start=element['unix_epoch_start'],
            unix_epoch_end=element['unix_epoch_end']
        )
        response.append(video_detail)
    return response
