from yt_concate.pipeline.steps.step import Step
from yt_concate.utils import Utils


class Preflight(Step):
    def process(self, data, inputs):
        Utils().create_dirs()
