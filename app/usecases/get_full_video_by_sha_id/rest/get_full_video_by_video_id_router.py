from fastapi import APIRouter

from app.usecases.get_full_video_by_sha_id.get_full_video_by_video_id_handler import get_full_video_by_sha_id

router = APIRouter()


@router.get("/collector/videos/")
async def collect_video_by_sha_id(sha_id: str):
    return await get_full_video_by_sha_id(sha_id=sha_id)
