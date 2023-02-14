from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        grp_sizes = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in grp_sizes:
                grp_sizes[groupSizes[i]] = []
            grp_sizes[groupSizes[i]].append(i)
        final_groups = []
        for size, indexes_arr in grp_sizes.items():
            if len(indexes_arr) > size:
                group = []
                for i in range(len(indexes_arr)):
                    if len(group) == size:
                        final_groups.append(group)
                        group = []
                    group.append(indexes_arr[i])
                final_groups.append(group)
            else:
                final_groups.append(indexes_arr)
        return final_groups


input = [[3, 3, 3, 3, 3, 1, 3], [2, 1, 3, 3, 3, 2]]
output = [[[5], [0, 1, 2], [3, 4, 6]], [[1], [0, 5], [2, 3, 4]]]
for i in range(len(output)):
    r = Solution().groupThePeople(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
