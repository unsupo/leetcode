import os
import re

import markdownify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Input:
    name_values = {}
    s = ""

    def __init__(self, input) -> None:
        s = ""
        inp = input.split(', ')
        for i in inp:
            r = i.split(' = ')
            self.name_values[r[0]] = r[1]

    def __str__(self) -> str:
        return self.s


class Example:
    name = ""
    input = ""
    output = ""
    explanation = ""

    def __init__(self, example) -> None:
        e = example.split('\n')
        for i in e:
            if '**Example' in i:
                self.name = i
            if '**Input:**' in i:
                self.input = Input(i.replace('**Input:** ', ''))
            if '**Output:**' in i:
                self.output = i.replace('**Output:** ', '')
            if '**Explanation:**' in i:
                self.explanation = i.replace('**Explanation:** ', '')

    def __str__(self) -> str:
        return '**{}**\n\n\n<pre>\n<b>Input:</b> {}\n<b>Output:</b> {}\n{}</pre>'.format(self.name, str(self.input),
                                                                                         self.output,
                                                                                         '<b>Output:</b> {}\n'.format(
                                                                                             self.explanation))


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
diff = metadata[0].text
up_votes = metadata[1].text
down_votes = metadata[2].text
description_data = soup.select('div[data-cy="question-title"]')[0].parent.parent.contents[1].contents[0].contents
description = ""
examples = []
example = ""
constraints = ""
follow_up = ""
desc = True
exam = False
cons = False
foll = False
for content in description_data:
    if '<p><strong>Example' in str(content):
        desc = False
        exam = True
        if example:
            examples.append(Example(example))
            example = ""
    if '<p><strong>Constraints:</strong></p>' == str(content):
        cons = True
        exam = False
    if '<strong>Follow-up:' in str(content):
        foll = True
        cons = False
    if desc: description += markdownify.markdownify(str(content), heading_style="ATX")
    if exam: example += markdownify.markdownify(str(content), heading_style="ATX")
    if cons: constraints += markdownify.markdownify(str(content), heading_style="ATX")
    if foll: follow_up += markdownify.markdownify(str(content), heading_style="ATX")
examples.append(Example(example))

# dumb way to get all data, doesn't work when trying to templatize tests and such
# main = soup.select('div[data-cy="question-detail-main-tabs"]')[0]
# h = markdownify.markdownify(str(main), heading_style="ATX")
color = "<span style=\"color:{color}\">{}</span>."
os.remove(dir_name + '/README.md')
with open(dir_name + '/README.md', 'w') as f:
    f.write(
        '# {}\n{} :thumbsup:{} :thumbsdown:{}<br/>\n\n---\n{}\n<br/>'.format(title, color.format(diff, color="green"),
                                                                             up_votes, down_votes, description))
    f.write('\n'.join([str(i) for i in examples]) + "\n\n")
    f.write(constraints + "\n\n")
    f.write("**Follow-up:** " + follow_up.split('**Follow-up:**')[1])

inputs = examples[0].input.name_values
testName = re.sub(r'[0-9\.]+', '', title.replace(' ', '_'))
with open(dir_name + '/solution.py', 'w') as f:
    f.write(
        '''class Solution(object):
    def {}(self, {}):
        """
        {}
        :rtype: {}
        """
        # Have solution here
        pass

        '''.format(testName, ', '.join(inputs.keys()),
                   '\n        '.join([':type '+i + ': ' + inputs[i] for i in inputs.keys()]),
                   examples[0].output)
    )
    i = 0
    for example in examples:
        f.write('''def test{}():
    assert Solution().{}({}) == {}

            '''.format(i, testName, ', '.join(example.input.name_values.values()), example.output)
        )
        i += 1
    f.write("if name == '__main__':\n\t{}".format('\n\t'.join(['test'+j+'()' for j in range(i)])))
