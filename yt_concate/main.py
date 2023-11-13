from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList


CHANNEL_ID = 'UCr90FXGOO8nAE9B6FAUeTNA'


def main():

    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
                GetVideoList,
            ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()
