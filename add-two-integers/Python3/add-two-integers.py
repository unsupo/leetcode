class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1+num2


input = [[12, 5], [-10, 4]]
output = [17, -6]
for i in range(len(input)):
    r = Solution().sum(*input[i])
    if r != output[i]:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
