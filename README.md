# 🎞 yt-concate-py
![PyPI - Downloads](https://img.shields.io/pypi/dm/yt-concate-py)
![PyPI - License](https://img.shields.io/pypi/l/yt-concate-py)
<a href="https://pypi.org/project/yt-concate-py/"><img src="https://img.shields.io/pypi/v/yt-concate-py" /></a>

*yt-concate-py* is a Python app to produce a consolidated video by concatenating YouTube video clips that mention a specific word from user's input.

## Description
YouTube is the largest and the most popular video-sharing platform.\
As a YouTube user and a python programmer, I was building something related to my interest with a tutorial, then *yt-concate-py* was born.\
With this app, you can easily extract and concatenate video clips by a topic word that interested you the most from a YouTube channel.

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


## Example

## Result

## Reference
- [Python Advanced Course on Udemy](https://www.udemy.com/course/pythonadvanced/)


