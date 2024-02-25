from yt_concate.pipeline.steps.step import Step
from yt_concate.model.yt import YT
from yt_concate.logger import logger


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        logger.info('INITIALIZING YT...')
        return [YT(video_link) for video_link in data]
