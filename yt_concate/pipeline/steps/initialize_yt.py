from yt_concate.pipeline.steps.step import Step
from yt_concate.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(video_link) for video_link in data]
