import json
import os
import re

import markdownify
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class Input:
    name_values = {}
    s = ""

    def __init__(self, input) -> None:
        self.s = input

    def __str__(self) -> str:
        return self.s

    def get_name_values(self):
        inp = self.s.split(', ')
        for i in inp:
            r = i.split(' = ')
            self.name_values[r[0]] = r[1]
        return self.name_values


class Example:
    name = ""
    input = ""
    output = ""
    explanation = ""

    def __init__(self, example) -> None:
        e = example.split('\n')
        for i in range(len(e)):
            if '**Example' in e[i]:
                self.name = e[i]
            if '**Input:**' in e[i]:
                self.input = Input(e[i].replace('**Input:** ', '')[:])
            if '**Output:**' in e[i]:
                self.output = e[i].replace('**Output:** ', '')
            if '**Explanation:**' in e[i]:
                self.explanation = e[i].replace('**Explanation:** ', '')

    def __str__(self) -> str:
        return '**{}**\n\n\n<pre>\n<b>Input:</b> {}\n<b>Output:</b> {}\n{}</pre>'.format(self.name, str(self.input),
                                                                                         self.output,
                                                                                         '<b>Explanation:</b> {}\n'.format(
                                                                                             self.explanation) if self.explanation else '')


def create_problem(problem):
    base_url = 'https://leetcode.com/problems/' + problem + '/'
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

    driver = get_webdriver(base_url)
    wait_for_page_by_css_selector(driver, 'div[data-cy="question-title"]')
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
    ab = []
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
    try:
        os.remove(dir_name + '/README.md')
    except FileNotFoundError:
        pass
    with open(dir_name + '/README.md', 'w') as f:
        f.write(
            '# {}\n{} :thumbsup:{} :thumbsdown:{}<br/>\n\n---\n{}\n<br/>'.format(title, color.format(diff,
                                                                                                     color="green" if diff == "Easy" else "yellow" if diff == "Medium" else "red"),
                                                                                 up_votes, down_votes, description))
        f.write('\n'.join([str(i) for i in examples]) + "\n\n")
        f.write(constraints + "\n\n")
        if follow_up:
            f.write("**Follow-up:** " + follow_up.split('**Follow-up:**')[1])

    inputs = examples[0].input.get_name_values()
    testName = re.sub(r'[0-9\.\(\)]+', '', title.replace(' ', '_'))
    with open(dir_name + '/solution.py', 'w') as f:
        f.write(
            '''class Solution(object):
        def {}(self, {}):
            """
            {}
            :rtype: {}
            """
            # Have solution here and remove pass
            pass
    
            '''.format(testName, ', '.join(inputs.keys()),
                       '\n        '.join([':type ' + i + ': ' + inputs[i] for i in inputs.keys()]),
                       examples[0].output)
        )
        i = 0
        for example in examples:
            f.write('''\ndef test{}():
        assert Solution().{}({}) == {}
    
                '''.format(i, testName, ', '.join(example.input.get_name_values().values()), example.output)
                    )
            i += 1
        f.write(
            "\nif __name__ == '__main__':\n    {}".format('\n    '.join(['test' + str(j) + '()' for j in range(i)])))


def wait_for_page_by_css_selector(driver, selector):
    delay = 30
    try:
        myElem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException as e:
        raise e


def get_webdriver(base_url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(base_url)
    return driver


class Problem:
    def __init__(self, headers, row):
        rows = [i for i in row.children]
        for r in range(len(rows)):
            setattr(self, headers[r], rows[r].text)


def parseRows(header_row):
    headers = []
    for header in header_row.children:
        headers.append(header.text)
    return headers

lock_svg = '<svg class="flex-0 -mt-1.5 h-5 w-5 text-gray-5 dark:text-gray-7" fill="currentColor" height="1em" viewbox="0 0 24 24" width="1em" xmlns="http://www.w3.org/2000/svg"><path clip-rule="evenodd" d="M7 8v2H6a3 3 0 00-3 3v6a3 3 0 003 3h12a3 3 0 003-3v-6a3 3 0 00-3-3h-1V8A5 5 0 007 8zm8 0v2H9V8a3 3 0 116 0zm-3 6a2 2 0 100 4 2 2 0 000-4z" fill-rule="evenodd"></path></svg>'
def get_problems():
    all_problems = 'https://leetcode.com/problemset/all/'
    driver = get_webdriver(all_problems)
    wait_for_page_by_css_selector(driver, 'div[role="rowgroup"] > div')
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # loop over all pages and save test names/link/acceptance/difficulty remove premium ones
    while not hasattr(soup.select('nav[role="navigation"]>button:last-child')[0].attrs, 'disabled'):
        wait_for_page_by_css_selector(driver, 'div[role="rowgroup"] > div')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        rows = soup.select('div[role="row"]')
        headers = parseRows(rows[0])
        problems = []
        for row in rows[1:]:
            problems.append(Problem(headers, row))
            # BeautifulSoup(driver.page_source, "html.parser").select('#__next > div > div > div.grid.grid-cols-4.gap-4.md\:grid-cols-3.lg\:grid-cols-4.lg\:gap-6 > div.col-span-4.z-base.md\:col-span-2.lg\:col-span-3 > div:nth-child(7) > div.-mx-4.md\:mx-0 > div > div > div.border-b.border-divider-border-2.dark\:border-dark-divider-border-2 > div > div:nth-child(4) > div > span')[0]
            # BeautifulSoup(driver.page_source, "html.parser").select('div[role="row"]')[1].text
        # paginate
        paginate = driver.find_element(By.CSS_SELECTOR, 'nav[role="navigation"]>button:last-child')
        try: # driver.execute_script("arguments[0].click();", driver.find_element(By.CSS_SELECTOR, 'nav[role="navigation"]>button:last-child'))
            driver.execute_script("arguments[0].click();", paginate)
            # paginate.click()
        except Exception as e:
            print(e)
        wait_for_page_by_css_selector(driver, 'div[role="rowgroup"] > div')
    driver.close()
    with open('problems.json', 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    get_problems()
