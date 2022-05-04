class Solution(object):
    def _Reverse_Integer(self, x):
        """
        :type x: 123
        :rtype: 321
        """
        if x > 2**31 - 1 or x < -2**31: return 0
        xx = str(x)
        r = int("-" + xx[:-len(xx):-1] if xx[0] == '-' else xx[::-1])
        if r > 2**31 - 1 or r < -2**31: return 0
        return r


def test0():
    assert Solution()._Reverse_Integer(123) == 321


def test1():
    assert Solution()._Reverse_Integer(-123) == -321


def test2():
    assert Solution()._Reverse_Integer(120) == 21


def test3():
    assert Solution()._Reverse_Integer(1534236469) == 0


def test4():
    assert Solution()._Reverse_Integer(900000) == 9


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
