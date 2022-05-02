import os

import requests
from bs4 import BeautifulSoup

base_url = 'https://leetcode.com/problems/two-sum/'
soup = BeautifulSoup(requests.get(base_url).content, "html.parser")
print(soup)
# key = soup.select_one("#ncaptchaRecaptchaId")["data-sitekey"]
# make directory for new problem
os.mkdir()
