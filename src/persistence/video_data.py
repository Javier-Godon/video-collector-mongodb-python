from dataclasses import dataclass


@dataclass
class VideoData:
    uuid: str
    sha_id: str
    element_id: str
    element_alias: str
    unix_epoch: int
    chunk_index: int
    data: str
