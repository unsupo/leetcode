class Solution(object):
    def _Longest_Substring_Without_Repeating_Characters(self, s):
        """
        :type s: "abcabcbb"
        :rtype: 3
        """
        l=""
        for i in s:
            
        # Have solution here and remove pass
        pass

        
def test0():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("abcabcbb") == 3

            
def test1():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("bbbbb") == 1

            
def test2():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("pwwkew") == 3

            
if __name__ == '__main__':
    test0()
    test1()
    test2()
