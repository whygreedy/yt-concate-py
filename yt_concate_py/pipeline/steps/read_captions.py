import time
import os

from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.settings import CAPTIONS_DIR
from yt_concate_py.logger import logger


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        logger.info('READING CAPTIONS...')
        for yt in data:
            logger.debug(f'reading yt : {yt.video_link}')
            filepath = os.path.join(CAPTIONS_DIR, yt.id + '.txt')
            is_file_exist = os.path.exists(filepath)
            if is_file_exist is not True:
                logger.debug(f'{is_file_exist}! caption file not found : {filepath}')
                continue
            captions = {}
            logger.debug(f'{is_file_exist}! caption file exists : {filepath}')
            with open(filepath, 'r', encoding='utf-8') as f:
                is_time = False
                timestamp = None
                caption = None
                for line in f:
                    line = line.strip()
                    if "-->" in line:
                        timestamp = line
                        is_time = True
                        continue
                    if is_time:
                        caption = line
                        is_time = False
                        captions[caption] = timestamp
            yt.captions = captions

        return data
