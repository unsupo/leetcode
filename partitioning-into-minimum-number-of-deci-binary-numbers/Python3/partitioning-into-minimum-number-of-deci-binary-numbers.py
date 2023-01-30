'''
Failed 1

curr = ''
count = 0
c = 0
isCount = False
while n != '0':
    for i in n:
        c += 1
        if i != '0':
            isCount = True
            curr += str(int(i) - 1)
        elif c>1 and curr != '0':
            curr += '0'
    c=0
    n = curr
    curr = ''
    if isCount: count += 1
return count

count=0
        while n != '0':
            takeAway = ''.join(len(n)*[str(1)])
            v = int(n) - int(takeAway)
            if v > 0:
                n = v
            else:
                n = int(n) - int(''.join((len(n)-1)*[str(1)])+'0')
            count+=1
            n=str(n)
        return count
'''

class Solution:
    def minPartitions(self, n: str) -> int:
        # greedily take away biggest that i can then smaller until 0 then backtrack if not possible
        # simpliest is best
        max='0'
        for i in n:
            if i == '9': return 9
            if i > max:
                max = i
        return int(max)


input = ["32", "82734", "27346209830709182346"]
output = [3, 8, 9]
for i in range(len(input)):
    r = Solution().minPartitions(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
