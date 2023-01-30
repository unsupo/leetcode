from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        zGrid = list(zip(*grid))
        cnt = 0
        for i in range(len(grid)):
            w = max(grid[i])
            for j in range(len(grid[i])):
                s = max(zGrid[j])
                cnt += min(w, s) - grid[i][j]
        return cnt


input = [[[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]
output = [35, 0]
for i in range(len(output)):
    r = Solution().maxIncreaseKeepingSkyline(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
