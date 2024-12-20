from dataclasses import dataclass
from typing import Optional


@dataclass
class GetVideoListRequest:
    unix_epoch_start: int
    unix_epoch_end: int
    sha_id: Optional[str] = None
    element_alias: Optional[str] = None
