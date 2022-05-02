import os

import requests
from bs4 import BeautifulSoup

base_url = 'https://leetcode.com/problems/two-sum/'
# make directory for new problem
dir_name = base_url.split('/')
if base_url[-1].replace('/',''):
    dir_name = base_url[-1]
else:
    dir_name = base_url[-2]
os.mkdir(dir_name)


soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
print(soup)
