import timeit


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        m = {}
        k = key.replace(' ', '')
        j = 0
        for i in range(len(k)):
            if k[i] in m: continue
            m[k[i]] = chr(j + 97)
            j += 1
        return ''.join([m[i] if i in k else i for i in message])

    def best_decodeMessage(self, key: str, message: str) -> str:
        dc = {}
        i = 0
        for c in key:
            if c == ' ':
                continue
            if c in dc:
                continue
            dc[c] = chr(i + 97)
            i += 1

        dec = ''
        for c in message:
            if c in dc:
                dec += dc[c]
            else:
                dec += c

        return dec


def test(m, silent=False):
    input = [["the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"], ["eljuxhpwnyrdgtqkviszcfmabo",
                                                                                   "zwx hnfx lqantp mnoeius ycgk vcnjrdb"]]
    output = ["this is a secret", "the five boxing wizards jump quickly"]
    for i in range(len(output)):
        r = m(*input[i])
        if str(r) != str(output[i]):
            raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
        if not silent:
            print('Passed input: ' + str(input[i]))


test(Solution().decodeMessage)

print(timeit.timeit(stmt=lambda: test(Solution().decodeMessage, True), number=1_000_000))
print(timeit.timeit(stmt=lambda: test(Solution().best_decodeMessage, True), number=1_000_000))
# 8.606729250008357
# 8.111053000000538
# same time