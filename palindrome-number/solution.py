class Solution(object):
    def _Palindrome_Number(self, x):
        """
        :type x: 121
        :rtype: true
        """
        xx = str(x)

        
def test0():
    assert Solution()._Palindrome_Number(121) == true

            
def test1():
    assert Solution()._Palindrome_Number(-121) == false

            
def test2():
    assert Solution()._Palindrome_Number(10) == false

            
if __name__ == '__main__':
    test0()
    test1()
    test2()
