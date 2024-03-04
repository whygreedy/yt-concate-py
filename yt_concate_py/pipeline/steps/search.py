from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.model.found import Found
from yt_concate_py.logger import logger


class Search(Step):
    def process(self, data, inputs, utils):
        logger.info('SEARCHING THE TERM...')
        search_term = inputs['search_term']
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_term in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        logger.info(f'found {len(found)} occurrences')
        logger.info(found)
        return found
