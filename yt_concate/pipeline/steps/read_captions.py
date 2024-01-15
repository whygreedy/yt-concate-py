import time
import os

from yt_concate.pipeline.steps.step import Step

from yt_concate.settings import CAPTIONS_DIR


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        print(f'Reading captions at {time.strftime("%Y-%m-%d %H:%M:%S")}')
        for yt in data:
            print(f'reading yt : {yt.video_link}')
            filepath = os.path.join(CAPTIONS_DIR, yt.id + '.txt')
            is_file_exist = os.path.exists(filepath)
            if is_file_exist is not True:
                print(f'{is_file_exist}! caption file not found : {filepath}')
                continue
            captions = {}
            print(f'{is_file_exist}! caption file exists : {filepath}')
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
