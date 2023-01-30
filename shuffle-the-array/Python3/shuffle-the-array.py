from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        r = []
        for i in range(len(nums)-n):
            r.append(nums[i])
            r.append(nums[i+n])
        return r


input = [[[2, 5, 1, 3, 4, 7], 3], [[1, 2, 3, 4, 4, 3, 2, 1], 4], [[1, 1, 2, 2], 2]]
output = [[2, 3, 5, 4, 1, 7], [1, 4, 2, 3, 3, 2, 4, 1], [1, 2, 1, 2]]
for i in range(len(input)):
    r = Solution().shuffle(*input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
