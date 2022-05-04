class Solution(object):
    def _String_to_Integer_atoi(self, s):
        """
        :type s: "42"
        :rtype: 42
        """
        num=""
        start=False
        for i in range(len(s)):
            if s[i] in ():
                start = True
            

        
def test0():
    assert Solution()._String_to_Integer_atoi("42") == 42

            
def test1():
    assert Solution()._String_to_Integer_atoi("   -42") == -42

            
def test2():
    assert Solution()._String_to_Integer_atoi("4193 with words") == 4193

            
if __name__ == '__main__':
    test0()
    test1()
    test2()
