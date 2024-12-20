import uvicorn
from fastapi import FastAPI

from app.configuration.configuration import get_data
from app.usecases.get_full_video_by_sha_id.rest import get_full_video_by_video_id_router
from app.usecases.get_video_list.rest import get_video_list_router

app = FastAPI()

app.include_router(router=get_full_video_by_video_id_router.router)
app.include_router(router=get_video_list_router.router)

port = get_data()['server']['port']

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
