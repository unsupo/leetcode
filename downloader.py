import os

import markdownify
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

base_url = 'https://leetcode.com/problems/two-sum/'
# make directory for new problem
dir_name = base_url.split('/')
if dir_name[-1].replace('/',''):
    dir_name = dir_name[-1]
else:
    dir_name = dir_name[-2]
try:
    os.mkdir(dir_name)
except FileExistsError:
    pass

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(base_url)

soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
# title=
# description=
# examples=
# contraints=
# followup=

h = markdownify.markdownify(soup, heading_style="ATX")

print(soup)
