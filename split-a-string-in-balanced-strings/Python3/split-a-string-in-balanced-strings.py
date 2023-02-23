import timeit
import random as r


class Solution:
    def is_balanced(self, s: str) -> bool:
        return len(s) // 2 == len(s.replace('R', ''))

    def balancedStringSplit(self, s: str) -> int:
        # letters can't be included in other substring if it's already included in one substring
        # must be greedy, get the largest substring then try to split it into the largest
        index_start = 0
        index_end = 2
        cnt = 0
        while index_end <= len(s):
            if self.is_balanced(s[index_start:index_end]):
                cnt += 1
                index_start = index_end
            index_end += 2
        return cnt

    def best_balancedStringSplit(self, s: str) -> int:
        d = {}
        res = 0
        for item in s:
            d[item] = d.get(item, 0) + 1
            if 'L' in d and 'R' in d and d['R'] == d['L']:
                res += 1
                d = {}
        return res


def test(m, silent=False):
    input = ["RLRRLLRLRL", "RLRRRLLRLL", "LLLLRRRR", "RLRRRLLRLL"]
    output = [4, 2, 1, 2]
    for i in range(len(output)):
        r = m(input[i])
        if str(r) != str(output[i]):
            raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
        if not silent:
            print('Passed input: ' + str(input[i]))


test(Solution().balancedStringSplit)


# determine what is faster
def singlePassCnt(s: str):
    r = 0
    l = 0
    for i in s:
        if i == 'R':
            r += 1
        else:
            l += 1
    return r == l


def strManipRmv(s: str):
    return len(s) // 2 == len(s.replace('R', ''))

# s = ''.join([r.choice(['R', 'L']) for i in range(1000)])
# assert singlePassCnt(s) == strManipRmv(s)
# print(timeit.timeit(stmt=lambda: singlePassCnt(s), number=100_000))
# print(timeit.timeit(stmt=lambda: strManipRmv(s), number=100_000))
# 3.3269041669991566
# 0.800605665994226
# string manip is almost 3x as fast

# print(timeit.timeit(stmt=lambda: test(Solution().balancedStringSplit, True), number=1_000_000))
# print(timeit.timeit(stmt=lambda: test(Solution().best_balancedStringSplit, True), number=1_000_000))
# 4.97332637499494
# 4.6712649169930955
# Roughly same time