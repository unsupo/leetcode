class Solution(object):
    def _Reverse_Integer(self, x):
        """
        :type x: 123
        :rtype: 321
        """
        xx = str(x)
        return "-" + xx[1::-1] if xx[0] == '-' else xx[::-1]


def test0():
    assert Solution()._Reverse_Integer(123) == 321


def test1():
    assert Solution()._Reverse_Integer(-123) == -321


def test2():
    assert Solution()._Reverse_Integer(120) == 21


if __name__ == '__main__':
    test0()
    test1()
    test2()