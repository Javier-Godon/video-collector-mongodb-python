import asyncio

from app.usecases.get_video_list.get_video_list_handler import get_video_list

asyncio.run(get_video_list(sha_id='cc28c1324eb299d5636f1e5198a374f51e0e0438b0c83aac0c7886d772cd7ff7',
               element_alias='INS352AR74', unix_epoch_start=11174744, unix_epoch_end=11174999))
