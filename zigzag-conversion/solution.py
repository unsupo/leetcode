class Solution(object):
    def _Zigzag_Conversion(self, s, numRows):
        """
        :type s: "PAYPALISHIRING"
        :type numRows: 3
        :rtype: "PAHNAPLSIIGYIR"
        """
        rows = ["" for i in range(numRows)]
        r = 0  # current row to add things to
        sr = numRows - 1  # sliding rows to fill the gaps
        for i in range(len(s)):
            if r >= numRows:
                r = 0
                for j in reversed(range(1, sr)):
                    rows[j] += s[i]
                    i += 1
            rows[r] += s[i]
            r += 1
        return ''.join(rows)


def test0():
    assert Solution()._Zigzag_Conversion("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"


def test1():
    assert Solution()._Zigzag_Conversion("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


def test2():
    assert Solution()._Zigzag_Conversion("A", 1) == "A"


if __name__ == '__main__':
    test0()
    test1()
    test2()
