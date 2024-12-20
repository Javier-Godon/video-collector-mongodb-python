from dataclasses import dataclass


@dataclass
class GetVideoListQuery:
    sha_id: str
    element_alias: str
    unix_epoch_start: int
    unix_epoch_end: int


