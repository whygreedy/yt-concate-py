from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.prefligt import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_captions import ReadCaptions
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():

    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
                Preflight,
                GetVideoList,
                DownloadCaptions,
                ReadCaptions,
            ]

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
