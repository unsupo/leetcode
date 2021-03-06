class Solution(object):
    def _Palindrome_Number(self, x):
        """
        :type x: 121
        :rtype: true
        """
        if x < 0: return False
        xx = str(x)
        l = len(xx) // 2 - 1
        r = len(xx) // 2
        if len(xx) % 2 != 0:
            r += 1
        while l >= 0 and r < len(xx):
            if xx[l] != xx[r]:
                return False
            l -= 1
            r += 1
        return True


def test0():
    assert Solution()._Palindrome_Number(121) == True


def test1():
    assert Solution()._Palindrome_Number(-121) == False


def test2():
    assert Solution()._Palindrome_Number(10) == False


if __name__ == '__main__':
    test0()
    test1()
    test2()
