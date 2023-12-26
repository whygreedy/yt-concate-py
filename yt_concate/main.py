from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.prefligt import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_captions import ReadCaptions
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
SEARCH_TERM = 'incredible'
LIMIT = 10


def main():

    inputs = {
        'channel_id': CHANNEL_ID,
        'search_term': SEARCH_TERM,
        'limit': LIMIT,
    }

    steps = [
                Preflight,
                GetVideoList,
                InitializeYT,
                DownloadCaptions,
                ReadCaptions,
                Search,
                DownloadVideos,
                EditVideo,
                Postflight,
            ]

    utils = Utils()

    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()
