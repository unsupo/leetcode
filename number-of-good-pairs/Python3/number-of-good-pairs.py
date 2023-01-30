from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        Good pairs are defined nums[i] == nums[j] and i<j
        :param nums: Array of numbers
        :return: number of good pairs
        """
        # this will be num and array of indexes with that num
        pairs = {}
        for i in range(len(nums)):
            if nums[i] not in pairs:
                pairs[nums[i]] = []
            pairs[nums[i]].append(i)
        # now we have each num with list of corresponding indexes
        pairArr = pairs.values()
        # now we need to get a count of each combination of pairs in each list from PairArr
        count = 0
        for p in pairArr:
            # sum(n-1) from 2 to l or sum(n) from 1 to l-1, sum(x)=x(x+1)/2 where x = l-1
            x = len(p)-1
            count += x * (x + 1) / 2
        return int(count)


input = [[1, 2, 3, 1, 1, 3], [1, 1, 1, 1], [1, 2, 3]]
output = [4, 6, 0]
for i in range(len(input)):
    r = Solution().numIdenticalPairs(input[i])
    if str(r) != str(output[i]):  # TODO this failed with 4.0 != 4 in leetcode but not here
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
