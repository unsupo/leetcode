class Solution(object):
    def _Longest_Palindromic_Substring(self, s):
        """
        :type s: "babad"
        :rtype: "bab"
        """
        for i in s:
            

        
def test0():
    assert Solution()._Longest_Palindromic_Substring("babad") == "bab"

            
def test1():
    assert Solution()._Longest_Palindromic_Substring("cbbd") == "bb"

            
if __name__ == '__main__':
    test0()
    test1()
