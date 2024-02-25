from yt_concate.pipeline.steps.step import Step
from yt_concate.logger import logger


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger.info('IN POSTFLIGHT...')
