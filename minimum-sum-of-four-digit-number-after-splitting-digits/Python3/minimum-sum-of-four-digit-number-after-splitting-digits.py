class Solution:
    def minimumSum(self, num: int) -> int:
        # split the num into unique chars
        # sort chars and return addition of concat of every other value
        r = []
        for c in str(num):
            r.append(c)
        r.sort()
        digits = 2
        nums = ['', '']
        for i in range(len(r)):
            nums[i % digits] += r[i]
        return sum([int(i) for i in nums])


input = [2932, 4009]
output = [52, 13]
for i in range(len(input)):
    r = Solution().minimumSum(input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
