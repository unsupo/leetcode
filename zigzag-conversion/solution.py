class Solution(object):
    def _Zigzag_Conversion(self, s, numRows):
        """
        :type s: "PAYPALISHIRING"
        :type numRows: 3
        :rtype: "PAHNAPLSIIGYIR"
        """
        rows = [[] for i in range(numRows)]
        for i in range(len(s)):
            pass # 3,1-4,2-5,3

        
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
