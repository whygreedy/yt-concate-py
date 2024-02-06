import time
import concurrent.futures

from pytubefix import YouTube
from pytubefix.cli import on_progress

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        yt_set = set([found.yt for found in data])
        print(f'downloading {len(yt_set)} videos...')

        yt_ = []
        for yt in yt_set:
            video_link = str(yt.video_link)

            if yt.video_file_exist:
                print(f'found existing video file : {video_link}, skipping...')
                continue
            else:
                yt_.append(yt)

        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(self.download_videos, yt_)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Total running time for downloading videos : {elapsed_time} seconds')

        return data

    def download_videos(self, yt):

        video_link = str(yt.video_link)
        youtube = YouTube(video_link, on_progress_callback=on_progress)
        ys = youtube.streams.get_highest_resolution()
        ys.download(output_path=VIDEOS_DIR, filename=yt.video_filename)
        print(f'download yt video : {video_link}')
