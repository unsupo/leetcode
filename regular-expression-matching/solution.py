class Solution(object):
    def _Regular_Expression_Matching(self, s, p):
        """
        :type s: "aa"
        :type p: "a"
        :rtype: false
        """
        for i in s:
            for j in p:
                

        
def test0():
    assert Solution()._Regular_Expression_Matching("aa", "a") == false

            
def test1():
    assert Solution()._Regular_Expression_Matching("aa", "a\*") == true

            
def test2():
    assert Solution()._Regular_Expression_Matching("ab", ".\*") == true

            
if __name__ == '__main__':
    test0()
    test1()
    test2()
