import re
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(re.split(r'\s+', i.strip())) for i in sentences])


input = [["alice and bob love leetcode", "i think so too", "this is great thanks very much"],
         ["please wait", "continue to fight", "continue to win"]]
output = [6, 3]
for i in range(len(input)):
    r = Solution().mostWordsFound(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
