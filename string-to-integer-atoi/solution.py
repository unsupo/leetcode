class Solution(object):
    def _String_to_Integer_atoi(self, s):
        """
        :type s: "42"
        :rtype: 42
        """
        s = s.strip()
        if len(s) == 0 or (len(s) > 1 and s[0] in ('+', '-') and s[1] in ('+', '-')): return 0
        if s[0] == '+': s = s[1:]
        num = ""
        for i in range(len(s)):
            if s[i] not in ('-', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                break
            num += s[i]
        if not num:
            return 0
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


def test4():
    assert Solution()._String_to_Integer_atoi("+-12") == 0


def test5():
    assert Solution()._String_to_Integer_atoi("-+12") == 0


def test6():
    assert Solution()._String_to_Integer_atoi("") == 0


def test7():
    assert Solution()._String_to_Integer_atoi("+") == 0


def test8():
    assert Solution()._String_to_Integer_atoi("-") == 0


def test9():
    assert Solution()._String_to_Integer_atoi("-+") == 0


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
