from pytubefix import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for video_link in data:
            yt = YouTube(video_link)
            subtitles = yt.captions.all()
            try:
                first_subtitle = subtitles[0]
                first_subtitle_code = first_subtitle.code

                caption = yt.captions.get_by_language_code(first_subtitle_code)
                caption_srt = caption.generate_srt_captions()

                filepath = utils.get_caption_path(video_link)
                with open(filepath, 'w') as f:
                    f.write(caption_srt)
            except IndexError:
                continue
