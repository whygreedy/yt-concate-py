import time
import os
import concurrent.futures

from pytubefix import YouTube

from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.settings import CAPTIONS_DIR
from yt_concate_py.logger import logger


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        logger.info('DOWNLOADING CAPTIONS...')
        start_time = time.time()
        yt_ = []
        for yt in data:
            if yt.caption_file_exist:
                logger.debug('found existing caption file')
                continue
            else:
                yt_.append(yt)

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            executor.map(self.download_captions, yt_)

        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.info('Completed downloading captions')
        logger.info(f'Downloaded {len(yt_)} new caption files')
        logger.info(f'Total running time for downloading captions : {elapsed_time} seconds')
        return data

    def download_captions(self, yt):
        logger.debug(f'downloading caption : {yt.video_link}')
        youtube = YouTube(yt.video_link)
        subtitles = list(youtube.captions)
        try:
            first_subtitle = subtitles[0]
            first_subtitle_code = first_subtitle.code
            caption = youtube.captions[first_subtitle_code]
            caption_srt = caption.generate_srt_captions()

            filepath = os.path.join(CAPTIONS_DIR, yt.id + '.txt')
            try:
                logger.debug(f'writing caption file for {filepath}')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(caption_srt)
                logger.debug(f'completed writing caption file for {filepath}')
                is_file_exist = os.path.exists(filepath)
                logger.debug(f'file exist or not: {is_file_exist}')
            except Exception as e:
                logger.error(f'error for writing caption file: {str(e)}')
        except IndexError:
            pass
