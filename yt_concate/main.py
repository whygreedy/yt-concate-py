from yt_concate.steps.step import Step
from yt_concate.steps.step import StepException
from yt_concate.steps.get_video_list import GetVideoList


CHANNEL_ID = 'UCr90FXGOO8nAE9B6FAUeTNA'

inputs = {
    'channel_id': CHANNEL_ID,
}

steps = [
    GetVideoList,
]

for step in steps:
    try:
        step().process(inputs)
    except StepException as e:
        print(e)
        break
