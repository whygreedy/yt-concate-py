from pytubefix import YouTube
from pytubefix.cli import on_progress

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print(f'downloading {len(yt_set)} videos...')
        for yt in yt_set:
            video_link = str(yt.video_link)

            if yt.video_file_exist:
                print(f'found existing video file : {video_link}, skipping...')
                continue

            youtube = YouTube(video_link, on_progress_callback=on_progress)
            ys = youtube.streams.get_highest_resolution()
            ys.download(output_path=VIDEOS_DIR, filename=yt.video_filename)
            print(f'download yt video : {video_link}')

        return data
