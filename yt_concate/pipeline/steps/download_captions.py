import os
from yt_concate.settings import CAPTIONS_DIR

from pytubefix import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.utils import Utils


class DownloadCaptions(Step):
    def process(self, data, inputs):
        video_link = 'https://www.youtube.com/watch?v=ZRHuv74T4Z8'
        yt = YouTube(video_link)
        yt_id = video_link.split("?v=")[1]
        filepath = os.path.join(CAPTIONS_DIR, yt_id + '.txt')

        subtitles = yt.captions.all()
        first_subtitle = subtitles[0]
        first_subtitle_code = first_subtitle.code

        caption = yt.captions.get_by_language_code(first_subtitle_code)
        caption_srt = caption.generate_srt_captions()

        with open(filepath, 'w') as f:
            f.write(caption_srt)
