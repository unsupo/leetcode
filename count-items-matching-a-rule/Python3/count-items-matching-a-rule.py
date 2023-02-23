from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return len([i for i in items if i[0 if ruleKey == 'type' else 1 if ruleKey == 'color' else 2] == ruleValue])


input = [[[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]], "color", "silver"],
         [[["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"]]
output = [1, 2]
for i in range(len(output)):
    r = Solution().countMatches(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
