from dataclasses import dataclass


@dataclass
class VideoDetailResponse:
    uuid: str
    element_alias: str
    unix_epoch_start: int
    unix_epoch_end: int


