from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.prefligt import Preflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():

    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
                Preflight,
                GetVideoList,
            ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
