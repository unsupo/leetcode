from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        t = 0
        for i in operations:
            if i == "++X" or i == "X++":
                t += 1
            if i == "--X" or i == "X--":
                t -= 1
        return t


input = [["--X", "X++", "X++"], ["++X", "++X", "X++"], ["X++", "++X", "--X", "X--"]]
output = [1, 3, 0]
for i in range(len(input)):
    r = Solution().finalValueAfterOperations(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
