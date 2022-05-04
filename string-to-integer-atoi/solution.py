class Solution(object):
    def _String_to_Integer_atoi(self, s):
        """
        :type s: "42"
        :rtype: 42
        """
        num = ""
        start = False
        for i in range(len(s)):
            if s[i] in ('-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                start = True
            elif start:
                break
            if start: num += s[i]
        r = int(num)
        if r > 2 ** 31 - 1: return 2 ** 31 - 1
        if r < -2 ** 31: return -2 ** 31
        return r


def test0():
    assert Solution()._String_to_Integer_atoi("42") == 42


def test1():
    assert Solution()._String_to_Integer_atoi("   -42") == -42


def test2():
    assert Solution()._String_to_Integer_atoi("4193 with words") == 4193


def test3():
    assert Solution()._String_to_Integer_atoi("words and 987") == 0


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
