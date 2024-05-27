# 🎞 yt-concate-py
![PyPI - Downloads](https://img.shields.io/pypi/dm/yt-concate-py)
![PyPI - License](https://img.shields.io/pypi/l/yt-concate-py)
<a href="https://pypi.org/project/yt-concate-py/"><img src="https://img.shields.io/pypi/v/yt-concate-py" /></a>

*yt-concate-py* is a Python app to produce a consolidated video by concatenating YouTube video clips that mention a specific word from user's input.

## Description
YouTube is the largest and the most popular video-sharing platform.\
As a YouTube user and a python programmer, I was building something related to my interest with a tutorial, then *yt-concate-py* was born.\
With this app, you can easily extract and concatenate video clips by a topic word that interested you the most from a YouTube channel.

For example, these are screenshots of the output video that concatenates video clips mentioned "taiwan" from the [YouTube channel of 莫彩曦Hailey](https://www.youtube.com/@haileymocaixi).
![resultImage](https://raw.githubusercontent.com/whygreedy/yt-concate-py/main/images/result.jpg)

## Features
- supports in all languages\
(As long as the language for a word is the same as the language for the first subtitle option of a video)
- supports for customizing the number of clips to be concatenated\
(Default number: 10)

## Quickstart

### Using the command line interface
Clone this repo from GitHub to your local directory
```bash
git clone https://github.com/whygreedy/yt-concate-py.git
```
Change directory to the repo folder just downloaded
```bash
cd yt-concate-py
```
Add `.env file` that includes *your YouTube Data API Key* to the repo folder
```
# your .env file
API_KEY=<your YouTube Data API Key>
```
Create venv
```bash
virtualenv venv
```
Activate venv
```bash
source venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Change directory to the folder that includes main.py file
```bash
cd yt_concate_py
```
Execute main.py file
```bash
python3 main.py -c <channel_id> -s <search_term> -l <limit>
```

> If you want to concatenate a large number of clips, you could change ulimit to 2048 in terminal with command line `ulimit -n 2048` to avoid error message [Errno 24] Too many open files

### Using yt-concate-py in a Python script
Create venv
```bash
virtualenv venv
```
Activate venv
```bash
source venv/bin/activate
```
Install from PyPI with pip
```bash
pip install yt-concate-py
```
Add `.env file` that includes *your YouTube Data API Key*
```
# your .env file
API_KEY=<your YouTube Data API Key>
```
Import the package and execute it with a Python Script
```python
# your Python script
from yt_concate_py import main

main.main()
```


## Example & Result
Using the command line interface

concatenate video clips that mentioned "BMW" from default [YouTube channel of Supercar Blondie](https://www.youtube.com/@SupercarBlondie)
```bash
python3 main.py -s BMW -l 20
```
![resultENImage](https://raw.githubusercontent.com/whygreedy/yt-concate-py/main/images/result_en_horizontal.jpg)

concatenate video clips that mentioned "可愛" from the [YouTube channel of 金魚腦Goldfish Brain](https://www.youtube.com/@goldfishbrain)
```bash
python3 main.py -c UCTT5gtQU5rX8sUQnZaBqiVw -s 可愛 -l 30
```
![resultZHImage](https://raw.githubusercontent.com/whygreedy/yt-concate-py/main/images/result_zh_horizontal.jpg)

## Reference
- [Python Advanced Course on Udemy](https://www.udemy.com/course/pythonadvanced/)


