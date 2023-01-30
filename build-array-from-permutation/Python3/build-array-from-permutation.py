class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]


input = [[0, 2, 1, 5, 3, 4], [5, 0, 1, 2, 3, 4]]
output = [[0, 1, 2, 4, 5, 3], [4, 5, 0, 1, 2, 3]]
for i in range(len(input)):
    r = Solution().buildArray(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
