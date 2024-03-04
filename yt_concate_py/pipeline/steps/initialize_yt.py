from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.model.yt import YT
from yt_concate_py.logger import logger


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        logger.info('INITIALIZING YT...')
        return [YT(video_link) for video_link in data]
