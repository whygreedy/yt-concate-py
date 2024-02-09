from yt_concate.logger import logger

from yt_concate.pipeline.steps.step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger.info('IN POSTFLIGHT...')
