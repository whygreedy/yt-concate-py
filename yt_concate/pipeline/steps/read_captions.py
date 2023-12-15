import os
from pprint import pprint

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                is_time = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if "-->" in line:
                        time = line
                        is_time = True
                        continue
                    if is_time:
                        caption = line
                        is_time = False
                        captions[caption] = time
            data[caption_file] = captions

        pprint(data)
        return data



