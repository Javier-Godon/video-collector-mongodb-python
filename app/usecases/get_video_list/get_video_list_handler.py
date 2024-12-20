from app.configuration.database_connection import MongoConnection
from app.usecases.get_video_list.get_video_list_query import GetVideoListQuery


async def get_video_list(get_video_list_query: GetVideoListQuery) -> list:
    sha_id = get_video_list_query.sha_id
    element_alias = get_video_list_query.element_alias
    unix_epoch_start = get_video_list_query.unix_epoch_start
    unix_epoch_end = get_video_list_query.unix_epoch_end
    mongodb_instance = MongoConnection().get_instance()
    collection = mongodb_instance['video']
    json_query = {
        "$or": [
            {"$and": [{"unix_epoch_start": {"$gte": unix_epoch_start}}, {"unix_epoch_end": {"$lte": unix_epoch_end}}]},
            {"$and": [{"unix_epoch_start": {"$lte": unix_epoch_start}},
                      {"unix_epoch_end": {"$gte": unix_epoch_start}}]},
            {"$and": [{"unix_epoch_start": {"$lte": unix_epoch_start}},
                      {"unix_epoch_end": {"$gte": unix_epoch_start}}]},
            {"$and": [{"unix_epoch_start": {"$lte": unix_epoch_end}}, {"unix_epoch_end": {"$gte": unix_epoch_end}}]}
        ]}
    if sha_id is not None and element_alias is not None:
        json_query = {
            "$and": [json_query, {"sha_id": sha_id}, {"element_alias": element_alias}, {"chunk_index": 0}]}
    if sha_id is not None and element_alias is None:
        json_query = {
            "$and": [json_query, {"sha_id": sha_id}, {"chunk_index": 0}]}
    if sha_id is None and element_alias is not None:
        json_query = {
            "$and": [json_query, {"element_alias": element_alias}, {"chunk_index": 0}]}
    if sha_id is None and element_alias is None:
        json_query = {
            "$and": [{"chunk_index": 0}]}

    found = list(collection.find(json_query))

    return found
