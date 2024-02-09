import os
from yt_concate.logger import logger

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import VIDEOS_DIR
from yt_concate.settings import OUTPUTS_DIR


class EditVideo(Step):
    def process(self, data, inputs, utils):
        logger.info('EDITING VIDEO...')
        clips = []
        for found in data:
            logger.info(f'{found.yt.video_link}')
            logger.info(f'{found.time}')
            start, end = self.parse_caption_time(found.time)
            logger.info(f'{start, end}')
            filepath = os.path.join(VIDEOS_DIR, found.yt.id + '.mp4')
            video = VideoFileClip(filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        final_clip = concatenate_videoclips(clips, method="compose")
        temp_audio_filepath = os.path.join(OUTPUTS_DIR, inputs['channel_id'] + '_' + inputs['search_term'] + 'TEMP.mp4')
        output_filepath = os.path.join(OUTPUTS_DIR, inputs['channel_id'] + '_' + inputs['search_term'] + '.mp4')
        final_clip.write_videofile(
            output_filepath,
            remove_temp=False,
            temp_audiofile=temp_audio_filepath,
            audio_codec="aac",
            codec='libx264',
        )
        logger.info('Completed editing video')

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    @staticmethod
    def parse_time_str(time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return float(h) * 3600 + float(m) * 60 + float(s) + float(ms) / 1000
