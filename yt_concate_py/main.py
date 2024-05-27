import sys
import getopt
sys.path.append('../')

from yt_concate_py.pipeline.pipeline import Pipeline
from yt_concate_py.pipeline.steps.prefligt import Preflight
from yt_concate_py.pipeline.steps.get_video_list import GetVideoList
from yt_concate_py.pipeline.steps.initialize_yt import InitializeYT
from yt_concate_py.pipeline.steps.download_captions import DownloadCaptions
from yt_concate_py.pipeline.steps.read_captions import ReadCaptions
from yt_concate_py.pipeline.steps.search import Search
from yt_concate_py.pipeline.steps.download_videos import DownloadVideos
from yt_concate_py.pipeline.steps.edit_video import EditVideo
from yt_concate_py.pipeline.steps.postflight import Postflight
from yt_concate_py.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'
SEARCH_TERM = 'incredible'
LIMIT = 10


def print_usage():
    print('python3 main.py -c <channel_id> -s <search_term> -l <limit>')
    print('python3 main.py --channel_id <channel_id> --search_term <search_term> --limit <limit>')

    print('python3 main.py OPTIONS')
    print('OPTIONS:')
    print('{:>10} {:<20}{}'.format('-c', '--channel_id', 'Channel id of YouTube channel to download videos'))
    print('{:>10} {:<20}{}'.format('-s', '--search_term', 'A search term used to extract video clips'))
    print('{:>10} {:<20}{}'.format('-l', '--limit', 'Maximum number of video clips to concatenate'))


def main():

    inputs = {
        'channel_id': CHANNEL_ID,
        'search_term': SEARCH_TERM,
        'limit': LIMIT,
    }

    short_opts = 'hc:s:l:'
    long_opts = 'help channel_id= search_term= limit='.split()

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print_usage()
            sys.exit(0)
        elif opt in ("-c", "--channel_id"):
            inputs['channel_id'] = arg
        elif opt in ("-s", "--search_term"):
            inputs['search_term'] = arg
        elif opt in ("-l", "--limit"):
            inputs['limit'] = arg
        else:
            print_usage()
            sys.exit(2)

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
