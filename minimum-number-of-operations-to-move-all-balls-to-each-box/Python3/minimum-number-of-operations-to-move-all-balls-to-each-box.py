import timeit
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        min_ops = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j] == '1':
                    min_ops[i] += abs(i - j)
        return min_ops

    # this solution moves all the boxes to the left then moves them all to the right
    # this reduces time complexity from O(n^2) to O(n)
    def best_minOperations(self, boxes: str) -> List[int]:
            ans = [0]*len(boxes)
            leftCount, leftCost, rightCount, rightCost, n = 0, 0, 0, 0, len(boxes)
            for i in range(1, n): # start with the next since first cost is 0
                if boxes[i-1] == '1': leftCount += 1 # check the previous one
                leftCost += leftCount # each step move to right, the cost increases by # of 1s on the left
                ans[i] = leftCost
            for i in range(n-2, -1, -1): # start with second from last since that move is 0
                if boxes[i+1] == '1': rightCount += 1 # check last since we'll have to move that one
                rightCost += rightCount
                ans[i] += rightCost
            return ans


input = ["110", "001011"]
output = [[1, 1, 3], [11, 8, 5, 4, 3, 4]]
for i in range(len(output)):
    r = Solution().best_minOperations(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))


# print(timeit.timeit(stmt=lambda: Solution().minOperations(input[1]), number=1_000_000))
# print(timeit.timeit(stmt=lambda: Solution().best_minOperations(input[1]), number=1_000_000))
# 2.618211125023663
# 1.1015200830297545