from yt_concate.pipeline.steps.step import Step
from yt_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        search_term = inputs['search_term']
        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_term in caption:
                    print('found')
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)

        print(found)
        return found
