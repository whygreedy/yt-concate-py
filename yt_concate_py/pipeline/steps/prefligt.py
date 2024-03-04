from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.logger import logger


class Preflight(Step):
    def process(self, data, inputs, utils):
        logger.info('IN PREFLIGHT...')
        channel_id = inputs['channel_id']
        search_term = inputs['search_term']
        logger.info(f'Prepare to concatenate video clips from YT channel {channel_id} with {search_term}...')
        utils.create_dirs()
