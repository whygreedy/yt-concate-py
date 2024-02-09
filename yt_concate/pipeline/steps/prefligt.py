from yt_concate.logger import logger

from yt_concate.pipeline.steps.step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        logger.info('IN PREFLIGHT...')
        channel_id = inputs['channel_id']
        search_term = inputs['search_term']
        logger.info(f'Prepare to concatenate video clips from YT channel {channel_id} with {search_term}...')
        utils.create_dirs()
