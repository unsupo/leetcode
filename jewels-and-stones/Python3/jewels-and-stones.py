class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set()
        for i in jewels:
            jewelSet.add(i)
        totalJewels = 0
        for i in stones:
            if i in jewelSet:
                totalJewels += 1
        return totalJewels


input = [["aA", "aAAbbbb"], ["z", "ZZ"]]  # TODO this should have been given separted by arrays
output = [3, 0]
for i in range(len(output)):
    r = Solution().numJewelsInStones(*input[i])  # TODO this should have had a star
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
