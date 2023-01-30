from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        runningSum = []
        for i in nums:
            sum += i
            runningSum.append(sum)
        return runningSum

input = [[1, 2, 3, 4], [1, 1, 1, 1, 1], [3, 1, 2, 10, 1]]
output = [[1, 3, 6, 10], [1, 2, 3, 4, 5], [3, 4, 6, 16, 17]]
for i in range(len(input)):
    r = Solution().runningSum(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
