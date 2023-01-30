import sys


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


class Codec:
    base = 'http://tinyurl.com'
    chars = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~:?#[]@!$&\'()*+,;=']
    m = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        # convert url to base 10 num
        h = hash('https://leetcode.com/problems/blah-blah')
        if h < 0:
            h += sys.maxsize
        short = ''.join([self.chars[i] for i in numberToBase(h, len(self.chars))])
        self.m[h] = {'l': longUrl, 's': short}
        self.m[hash(short)] = h
        return short

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.m[self.m[hash(shortUrl)]]['l']


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

input = ["https://leetcode.com/problems/design-tinyurl"]
output = ["https://leetcode.com/problems/design-tinyurl"]
for i in range(len(output)):
    r = Codec().encode(input[i])
    print('Tiny URL: ' + r)
    o = Codec().decode(r)
    if str(o) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
