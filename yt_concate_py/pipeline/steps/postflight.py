from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.logger import logger


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger.info('IN POSTFLIGHT...')
