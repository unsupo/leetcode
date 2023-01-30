from typing import List  # TODO this wasn't imported


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mostCandies = max(candies) - extraCandies
        return [i >= mostCandies for i in candies]


# ni+k >= max(n)

input = [[[2, 3, 5, 1, 3], 3], [[4, 2, 1, 1, 2], 1],
         [[12, 1, 12], 10]]  # This was a 1d array needed to manually create sub arrays
output = [[True, True, True, False, True], [True, False, False, False, False],
          [True, False, True]]  # TODO these were lowercased
for i in range(len(output)):
    r = Solution().kidsWithCandies(*input[i])  # TODO this wasn't starred
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
