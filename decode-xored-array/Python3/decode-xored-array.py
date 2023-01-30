import timeit
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        # encoded[i]=arr[i] ^ arr[i+1], first is arr[0]
        # thus arr[i+1]=encoded[i]^arr[i]=>encoded[0]^first=arr[1]
        arr = [first]
        for i in encoded:
            arr.append(arr[-1] ^ i)
        return arr

    def decode_best(self, encoded: List[int], first: int) -> List[int]:
        ans = [] * (len(encoded) + 1)
        for i in encoded:
            temp = first
            ans.append(temp)
            temp = i ^ first
            first = temp
        ans.append(temp)
        return ans


input = [[[1, 2, 3], 1], [[6, 2, 7, 3], 4]]
output = [[1, 0, 2, 1], [4, 2, 0, 7, 4]]
for i in range(len(output)):
    r = Solution().decode_best(*input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

print(timeit.timeit(stmt=lambda: Solution().decode(*input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().decode_best(*input[0]), number=1_000_000))
