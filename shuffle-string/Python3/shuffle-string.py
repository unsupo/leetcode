from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join([
                s[i[0]] for i in
                sorted([(i, indices[i]) for i in range(len(indices))], key=lambda x: x[1])
            ])


input = [["codeleet", [4, 5, 6, 7, 0, 2, 1, 3]], ["abc", [0, 1, 2]]]
output = ["leetcode", "abc"]
for i in range(len(output)):
    r = Solution().restoreString(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
