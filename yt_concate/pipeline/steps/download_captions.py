import os

from pytubefix import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.utils import Utils
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs):
        for video_link in data:
            yt = YouTube(video_link)
            yt_id = video_link.split("?v=")[1]
            filepath = os.path.join(CAPTIONS_DIR, yt_id + '.txt')

            subtitles = yt.captions.all()
            try:
                first_subtitle = subtitles[0]
                first_subtitle_code = first_subtitle.code

                caption = yt.captions.get_by_language_code(first_subtitle_code)
                caption_srt = caption.generate_srt_captions()

                with open(filepath, 'w') as f:
                    f.write(caption_srt)
            except IndexError:
                continue
