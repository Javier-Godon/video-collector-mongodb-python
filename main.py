import uvicorn
from fastapi import FastAPI

from configuration.configuration import get_data
from src.usecases.get_full_video_by_video_id.router import router

app = FastAPI()

app.include_router(router=router)

port = get_data()['server']['port']

# @app.get("/")
# async def root():
#     return {"message": "Hello Bigger Applications!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
