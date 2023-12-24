from yt_concate.pipeline.steps.step import Step


class ReadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not yt.caption_file_exist:
                continue
            captions = {}
            with open(yt.caption_path, 'r') as f:
                is_time = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if "-->" in line:
                        time = line
                        is_time = True
                        continue
                    if is_time:
                        caption = line
                        is_time = False
                        captions[caption] = time
            yt.captions = captions

        return data
