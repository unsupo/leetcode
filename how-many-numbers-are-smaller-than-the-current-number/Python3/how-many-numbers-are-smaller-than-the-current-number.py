import timeit
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        return [s.index(i) for i in nums]

    def best(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        smaller_count = {}
        for i in range(len(sorted_nums)-1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            if next_num < curr_num:
                remaining_values = len(sorted_nums) - (i+1)
                smaller_count[curr_num] = remaining_values
            smaller_count[sorted_nums[-1]] = 0

        output = []
        for num in nums:
            output.append(smaller_count[num])
        return output

    def alt(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        d = {}
        result = []

        for index, num in enumerate(sorted_nums):
            if num not in d:
                d[num] = index

        for num in nums:
            result.append(d[num])

        return result


input = [[8, 1, 2, 2, 3], [6, 5, 4, 8], [7, 7, 7, 7]]
output = [[4, 0, 1, 1, 3], [2, 1, 0, 3], [0, 0, 0, 0]]
for i in range(len(output)):
    r = Solution().smallerNumbersThanCurrent(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))


print(timeit.timeit(stmt=lambda: Solution().best2(input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().smallerNumbersThanCurrent(input[0]), number=1_000_000))