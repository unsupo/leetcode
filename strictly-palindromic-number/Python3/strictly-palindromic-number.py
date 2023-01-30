from typing import List


def convertToBase(n: int, b: int) -> List[int]:
    if n == 0: return [0]
    r = []
    while n:
        r.append(int(n % b))
        n //= b
    return r[::-1]


def isPalandromic(n: List[int]) -> bool:
    return n == n[::-1]


class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # for i in range(2, n - 1):
        #     if not isPalandromic(convertToBase(n, i)):
        #         return False
        # return True
        return False

'''
r=sum(dib^i,0,n)
where 0<di<b-1

r=n%b+n//b
di+di*b^2

b(r,r-1)=11
r>2

b(r,r-2)=12
r>3

b(r,r-n)=1n
r>n+1

2n+1

l=100; n=1198; [convertToBase(i,i-n) for i in range(2*n+1,2*n+1+l)]
'''

input = [9, 4]
output = [False, False]
for i in range(len(output)):
    r = Solution().isStrictlyPalindromic(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
