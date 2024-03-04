import os

from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.settings import VIDEOS_DIR
from yt_concate_py.settings import OUTPUTS_DIR
from yt_concate_py.logger import logger


class EditVideo(Step):
    def process(self, data, inputs, utils):
        logger.info('EDITING VIDEO...')
        clips = []
        i = 0
        for found in data:
            logger.debug(f'{found.yt.video_link}')
            logger.debug(f'{found.time}')
            start, end = self.parse_caption_time(found.time)
            logger.debug(f'{start, end}')
            filepath = os.path.join(VIDEOS_DIR, found.yt.id + '.mp4')
            if not os.path.exists(filepath):
                logger.info(f'video file not found: {filepath}')
                continue
            try:
                video = VideoFileClip(filepath)
                if end > video.duration:
                    logger.info(f'end time exceeds video duration for {filepath}, adjusting {end} to {video.duration}')
                    end = video.duration
                video = VideoFileClip(filepath).subclip(start, end)
                clips.append(video)
                i += 1
                logger.info(f'clip has been added {filepath}, {start, end}, {i}')
                if len(clips) >= int(inputs['limit']):
                    break
            except Exception as e:
                logger.info(f'error for editing video {filepath}, {start, end} and the error is {str(e)}')
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
