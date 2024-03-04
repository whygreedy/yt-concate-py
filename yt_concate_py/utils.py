import os

from yt_concate_py.settings import DOWNLOADS_DIR
from yt_concate_py.settings import CAPTIONS_DIR
from yt_concate_py.settings import VIDEOS_DIR
from yt_concate_py.settings import OUTPUTS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)
        os.makedirs(OUTPUTS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_output_video_filepath(self, channel_id, search_term):
        filename = channel_id + '_' + search_term + '.mp4'
        return os.path.join(OUTPUTS_DIR, filename)

    def get_temp_audio_filepath(self, channel_id, search_term):
        filename = channel_id + '_' + search_term + 'TEMP_MPY_wvf_snd.mp4'
        return os.path.join(OUTPUTS_DIR, filename)
