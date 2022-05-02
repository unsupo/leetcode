import os

import requests
from bs4 import BeautifulSoup

base_url = 'https://leetcode.com/problems/two-sum/'
# make directory for new problem
dir_name = base_url.split('/')
if dir_name[-1].replace('/',''):
    dir_name = dir_name[-1]
else:
    dir_name = dir_name[-2]
os.mkdir(dir_name)


soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
h = markdownify.markdownify(html, heading_style="ATX")

print(soup)
