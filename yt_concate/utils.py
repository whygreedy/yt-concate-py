import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class Utils:
    def __init__(self):
        pass

    def create_dirs(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    def get_video_list_filepath(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_video_id(video_link):
        return video_link.split("?v=")[1]

    def get_caption_path(self, video_link):
        return os.path.join(CAPTIONS_DIR, self.get_video_id(video_link) + '.txt')

    def caption_file_exist(self, video_link):
        path = self.get_caption_path(video_link)
        return os.path.exists(path) and os.path.getsize(path) > 0
