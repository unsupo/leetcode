from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        return [pref[0]] + [pref[i] ^ pref[i + 1] for i in range(len(pref)-1)]


input = [[5, 2, 0, 3, 1], [13]]
output = [[5, 7, 2, 3, 2], [13]]
for i in range(len(output)):
    r = Solution().findArray(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
