class Solution(object):
    def _Palindrome_Number(self, x):
        """
        :type x: 121
        :rtype: true
        """
        if x < 0: return False
        xx = str(x)
        l=len(xx)//2
        r=len(xx)//2
        if l+r < len(x):
            r+=1
        while True:
            if l < 0 or r > len(xx):
                break
            

        
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
