import os

from yt_concate_py.settings import CAPTIONS_DIR
from yt_concate_py.settings import VIDEOS_DIR


class YT:
    def __init__(self, video_link):
        self.video_link = video_link
        self.id = self.get_video_id(self.video_link)
        self.caption_path = self.get_caption_path()
        self.caption_file_exist = self.caption_file_exist()
        self.video_path = self.get_video_path()
        self.video_filename = self.get_video_filename()
        self.video_file_exist = self.video_file_exist()
        self.captions = None


    @staticmethod
    def get_video_id(video_link):
        return video_link.split("?v=")[1]

    def get_caption_path(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.txt')

    def caption_file_exist(self):
        path = self.caption_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    def get_video_path(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def get_video_filename(self):
        return self.id + '.mp4'

    def video_file_exist(self):
        path = self.video_path
        return os.path.exists(path) and os.path.getsize(path) > 0

    def __str__(self):
        return '<YT(' + self.video_link + ')>'

    def __repr__(self):
        content = ':'.join(
            [
                'id=' + str(self.id),
                'caption_path=' + str(self.caption_path),
                'video_path=' + str(self.video_path)
            ]
        )
        return '<found(' + content + ')>'
