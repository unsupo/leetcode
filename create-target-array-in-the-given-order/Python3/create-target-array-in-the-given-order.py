import timeit
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, n in zip(index, nums):
            target.insert(i, n)
        return target

    def alt(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(index)):
            target.insert(index[i], nums[i])
        return target

    def alt2(self, nums: List[int], index: List[int]) -> List[int]:
        target = [0]*(len(index)-1)

        for i in range(len(nums)):
            currentIndex = index[i]
            target = target[:currentIndex]+[nums[i]]+target[currentIndex:]
        return target[:len(index)]


input = [[[0, 1, 2, 3, 4], [0, 1, 2, 2, 1]], [[1, 2, 3, 4, 0], [0, 1, 2, 3, 0]], [[1], [0]]]
output = [[0, 4, 1, 3, 2], [0, 1, 2, 3, 4], [1]]
for i in range(len(output)):
    r = Solution().alt2(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

print(timeit.timeit(stmt=lambda: Solution().createTargetArray(*input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().alt(*input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().alt2(*input[0]), number=1_000_000))
