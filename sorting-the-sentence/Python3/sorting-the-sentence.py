import re


class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split(' ')
        l.sort(key=lambda k: int(re.findall(r'[0-9]+', k)[0]))
        return ' '.join([re.findall(r'[A-Za-z]+', i)[0] for i in l])


input = ["is2 sentence4 This1 a3", "Myself2 Me1 I4 and3"]
output = ["This is a sentence", "Me Myself and I"]
for i in range(len(output)):
    r = Solution().sortSentence(input[i])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
