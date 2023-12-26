from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips

from yt_concate.pipeline.steps.step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            print(found.time)
            start, end = self.parse_caption_time(found.time)
            video = VideoFileClip(found.yt.video_path).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break
        final_clip = concatenate_videoclips(clips, method="compose")
        temp_audio_filepath = utils.get_temp_audio_filepath(inputs['channel_id'], inputs['search_term'])
        output_filepath = utils.get_output_video_filepath(inputs['channel_id'], inputs['search_term'])
        final_clip.write_videofile(
            output_filepath, remove_temp=False, temp_audiofile=temp_audio_filepath, audio_codec="aac", codec='libx264')

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    @staticmethod
    def parse_time_str(time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), int(s) + int(ms)/1000
