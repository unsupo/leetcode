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
if dir_name[-1].replace('/',''):
    dir_name = dir_name[-1]
else:
    dir_name = dir_name[-2]
try:
    os.mkdir(dir_name)
except FileExistsError:
    pass

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(base_url)
delay=3
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-cy="question-title"]')))
except TimeoutException as e:
    raise e
soup = BeautifulSoup(driver.page_source, "html.parser")
title = soup.select('div[data-cy="question-title"]')
# title=
# description=
# examples=
# contraints=
# followup=

h = markdownify.markdownify(soup, heading_style="ATX")

print(soup)
