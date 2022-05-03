class Solution(object):
    def _Longest_Palindromic_Substring(self, s):
        """
        :type s: "babad"
        :rtype: "bab"
        """
        if s == s[::-1]:
            return s
        l = []
        for i in range(len(s)):
            

        
def test0():
    assert Solution()._Longest_Palindromic_Substring("babad") == "bab"

            
def test1():
    assert Solution()._Longest_Palindromic_Substring("cbbd") == "bb"

            
if __name__ == '__main__':
    test0()
    test1()
