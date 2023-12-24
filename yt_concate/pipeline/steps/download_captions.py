from pytubefix import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if yt.caption_file_exist:
                print('found existing caption file')
                continue
            youtube = YouTube(yt.video_link)
            subtitles = youtube.captions.all()
            try:
                first_subtitle = subtitles[0]
                first_subtitle_code = first_subtitle.code

                caption = youtube.captions.get_by_language_code(first_subtitle_code)
                caption_srt = caption.generate_srt_captions()

                filepath = yt.caption_path
                with open(filepath, 'w') as f:
                    f.write(caption_srt)
            except IndexError:
                continue

        return data
