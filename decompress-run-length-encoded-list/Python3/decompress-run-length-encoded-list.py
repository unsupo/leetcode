import timeit
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]: # this is faster
        decomp = []
        for i in range(0, len(nums) - 1, 2):
            decomp.extend([nums[i + 1]] * nums[i])
        return decomp

    def alt(self, nums: List[int]) -> List[int]:
        decomp = []
        for i in range(0, len(nums) - 1, 2):
            for j in range(nums[i]):
                decomp.append(nums[i + 1])
        return decomp


input = [[1, 2, 3, 4], [1, 1, 2, 3]]
output = [[2, 4, 4, 4], [1, 3, 3]]
for i in range(len(output)):
    r = Solution().decompressRLElist(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

print(timeit.timeit(stmt=lambda: Solution().decompressRLElist(input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().alt(input[0]), number=1_000_000))
