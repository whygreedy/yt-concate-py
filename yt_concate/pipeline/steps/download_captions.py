import time
import os
from threading import Thread

from pytubefix import YouTube
from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import CAPTIONS_DIR


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):

        print(f'Downloading captions at {time.strftime("%Y-%m-%d %H:%M:%S")}')

        start_time = time.time()

        yt_list = []
        for yt in data:
            if yt.caption_file_exist:
                print('found existing caption file')
                continue
            else:
                yt_list.append(yt)

        thread_num = os.cpu_count()
        print(f'thread_num: {thread_num}')
        threads = []

        for i in range(thread_num):
            split_data = yt_list[i::thread_num]
            threads.append(Thread(target=self.download_captions, args=(split_data,)))
            threads[i].start()

        for thread in threads:
            thread.join()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'{len(yt_list)}')
        print(f'Total running time for downloading captions : {elapsed_time} seconds')
        print(f'Completed downloading captions at {time.strftime("%Y-%m-%d %H:%M:%S")}')
        return data

    def download_captions(self, split_data):
        for yt in split_data:
            print(f'downloading caption : {yt.video_link}')
            youtube = YouTube(yt.video_link)
            subtitles = youtube.captions.all()
            try:
                first_subtitle = subtitles[0]
                first_subtitle_code = first_subtitle.code

                caption = youtube.captions.get_by_language_code(first_subtitle_code)
                caption_srt = caption.generate_srt_captions()

                filepath = os.path.join(CAPTIONS_DIR, yt.id + '.txt')
                try:
                    print(f'writing caption file for {filepath}')
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(caption_srt)
                    print(f'completed writing caption file for {filepath}')
                    is_file_exist = os.path.exists(filepath)
                    print(f'file exist or not: {is_file_exist}')
                except Exception as e:
                    print(f'error for writing caption file: {str(e)}')
            except IndexError:
                continue
