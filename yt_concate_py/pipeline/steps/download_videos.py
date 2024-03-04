import time
import concurrent.futures

from pytubefix import YouTube
from pytubefix.cli import on_progress

from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.settings import VIDEOS_DIR
from yt_concate_py.logger import logger


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        logger.info('DOWNLOADING VIDEOS...')

        yt_set = set([found.yt for found in data])
        logger.info(f'prepare for downloading {len(yt_set)} videos...')

        yt_ = []
        for yt in yt_set:
            video_link = str(yt.video_link)

            if yt.video_file_exist:
                logger.debug(f'found existing video file : {video_link}, skipping...')
                continue
            else:
                yt_.append(yt)

        start_time = time.time()

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(self.download_videos, yt_)

        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info('Completed downloading all videos')
        logger.info(f'Total running time for downloading videos : {elapsed_time} seconds')

        return data

    def download_videos(self, yt):
        video_link = str(yt.video_link)
        logger.debug(f'prepare to download yt video : {video_link}')
        youtube = YouTube(video_link, on_progress_callback=on_progress)
        ys = youtube.streams.get_highest_resolution()
        ys.download(output_path=VIDEOS_DIR, filename=yt.video_filename)
        logger.debug(f'completely downloaded yt video : {video_link}')
