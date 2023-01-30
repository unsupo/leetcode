from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums


input = [[1, 2, 1], [1, 3, 2, 1]]
output = [[1, 2, 1, 1, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]]
for i in range(len(input)):
    r = Solution().getConcatenation(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
