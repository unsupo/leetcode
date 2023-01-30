import operator
import timeit
from functools import reduce
from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        m = map(int, str(n))
        s = map(int, str(n))  # slightly faster to use 2 maps

        def mult(l: List[int]):
            m = 1
            for i in l:
                m *= i
            return m

        return mult(m) - sum(s)

    def other(self, n: int) -> int:
        A = map(int, str(n))  # same as but with iter [int(i) for i in str(n)]
        B = map(int, str(n))  # same as but with iter [int(i) for i in str(n)]
        return reduce(operator.mul, A) - sum(B)  # this is slower than above

    def alter(self, n: int) -> int:
        return eval("*".join(str(n)) + "-(" + "+".join(str(n))+")")

    def best(self, n: int) -> int:
        prod = 1
        s = 0
        while n != 0:
            x = n % 10 # extracts out the last digit
            prod = prod * x # takes a running mult
            s = s + x # takes a running add
            n = n // 10 # removes the last digit
        return prod - s


input = [234, 4421]
output = [15, 21]
for i in range(len(output)):
    r = Solution().best(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

print(timeit.timeit(stmt=lambda: Solution().best(input[0]), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().subtractProductAndSum(input[0]), number=1_000_000))
