import urllib.request
import json

from yt_concate_py.pipeline.steps.step import Step
from yt_concate_py.settings import API_KEY
from yt_concate_py.logger import logger


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        logger.info('GETTING VIDEO LIST...')
        channel_id = inputs['channel_id']
        api_key = API_KEY

        if utils.video_list_file_exist(channel_id):
            logger.debug('found existing video list file')
            return self.read_file(utils.get_video_list_filepath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                            channel_id)

        video_links = []
        url = first_url

        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_link = base_video_url + i['id']['videoId']
                    if video_link not in video_links:
                        video_links.append(video_link)

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break

        self.write_to_file(video_links, channel_id, utils)
        logger.info(f'{len(video_links)} videos from this channel')
        logger.debug(video_links)
        return video_links

    def write_to_file(self, video_links, channel_id, utils):
        filepath = utils.get_video_list_filepath(channel_id)
        with open(filepath, 'w') as f:
            for video_link in video_links:
                f.write(video_link + '\n')

    def read_file(self, filepath):
        video_links = []
        with open(filepath, 'r') as f:
            for line in f:
                video_links.append(line.strip())
        return video_links
