from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        uniq = sorted(list(set([i[0] for i in points])))
        m = 0
        for i in range(len(uniq) - 1):
            v = uniq[i + 1] - uniq[i]
            if v > m:
                m = v
        return m


input = [[[8, 7], [9, 9], [7, 4], [9, 7]], [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]],
         [[1, 5], [1, 70], [3, 1000], [55, 700], [999876789, 53], [987853567, 12]]]
output = [1, 3, 987853512]
for i in range(len(output)):
    i=2
    r = Solution().maxWidthOfVerticalArea(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
