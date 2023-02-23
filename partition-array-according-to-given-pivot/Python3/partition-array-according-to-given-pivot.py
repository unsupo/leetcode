from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a=[]
        c=[]
        b=[]
        for i in nums:
            if i < pivot:
                a.append(i)
            elif i == pivot:
                b.append(i)
            else:
                c.append(i)
        return a+b+c


input = [[[9, 12, 5, 10, 14, 3, 10], 10], [[-3, 4, 3, 2], 2]]
output = [[9, 5, 3, 10, 10, 12, 14], [-3, 2, 4, 3]]
for i in range(len(output)):
    r = Solution().pivotArray(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
