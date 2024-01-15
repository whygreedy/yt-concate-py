import os
import time
from threading import Thread


from pytubefix import YouTube
from pytubefix.cli import on_progress

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        print(f'Downloading videos at {time.strftime("%Y-%m-%d %H:%M:%S")}')

        start_time = time.time()

        yt_set = set([found.yt for found in data])
        yt_list = list(yt_set)
        print(f'downloading {len(yt_list)} videos...')

        thread_num = os.cpu_count()
        threads = []
        print(f'thread_num: {thread_num}')

        for i in range(thread_num):
            split_data = yt_list[i::thread_num]
            threads.append(Thread(target=self.download_videos, args=(split_data, )))
            threads[i].start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Total running time for downloading videos : {elapsed_time} seconds')

        return data

    @staticmethod
    def download_videos(split_data):

        for yt in split_data:
            video_link = str(yt.video_link)

            if yt.video_file_exist:
                print(f'found existing video file : {video_link}, skipping...')
                continue

            try:
                youtube = YouTube(video_link, on_progress_callback=on_progress)
                ys = youtube.streams.get_highest_resolution()
                ys.download(output_path=VIDEOS_DIR, filename=yt.video_filename)
                print(f'completed downloading yt video : {video_link}')
            except Exception as e:
                print(f'Error! downloading video {video_link}: {e}')
