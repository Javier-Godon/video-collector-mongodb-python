from dataclasses import dataclass


@dataclass
class GetSummaryByVideoIdResponse:
    uuid: str
    number_of_chunks: str
    number_of_bytes_by_chunk: map
