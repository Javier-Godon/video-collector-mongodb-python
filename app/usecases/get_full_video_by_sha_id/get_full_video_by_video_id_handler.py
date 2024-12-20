import base64

import pymongo

from app.configuration.database_connection import MongoConnection


async def get_full_video_by_sha_id(sha_id: str):
    mongodb_instance = MongoConnection().get_instance()
    collection = mongodb_instance['video']
    json_query = {"sha_id": sha_id}
    found = collection.find(json_query)
    found.sort([('chunk_index', pymongo.ASCENDING)])
    found.distinct('chunk_index')
    full_video = bytearray()
    for video_data in found:
        base64_data_get = video_data.get('data')
        data_get = base64.b64decode(base64_data_get)
        full_video.extend(data_get)
    file = open('80MbSample.webm', 'wb')
    file.write(full_video)
    file.close()
