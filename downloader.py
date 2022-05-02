import os

import markdownify
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://leetcode.com/problems/two-sum/'
# make directory for new problem
dir_name = base_url.split('/')
if dir_name[-1].replace('/', ''):
    dir_name = dir_name[-1]
else:
    dir_name = dir_name[-2]
try:
    os.mkdir(dir_name)
except FileExistsError:
    pass

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(base_url)
delay = 30
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-cy="question-title"]')))
except TimeoutException as e:
    raise e
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.close()
title = soup.select('div[data-cy="question-title"]')[0].contents[0]
metadata = soup.select('div[data-cy="question-title"]')[0].parent.contents[1].contents
diff=metadata[0].text
up_votes=metadata[1].text
down_votes=metadata[2].text
description_data=soup.select('div[data-cy="question-title"]')[0].parent.parent.contents[1].contents[0].contents
description=""
desc = True
for content in description_data:
    if '<p><strong>Example' in content.text:
        desc=False
    if desc: description+=content.text

# examples=
# contraints=
# followup=
# dumb way to get all data, doesn't work when trying to templatize tests and such
main = soup.select('div[data-cy="question-detail-main-tabs"]')[0]
h = markdownify.markdownify(str(main), heading_style="ATX")

with open(dir_name + '/README.md') as f:
    f.write(h)
