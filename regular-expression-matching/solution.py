class Solution(object):
    def _Regular_Expression_Matching(self, s, p):
        """
        :type s: "aa"
        :type p: "a"
        :rtype: false
        """
        if p == '.*': return True
        expand = False
        expand_char = ""
        for i in range(len(s)):
            if s[i] != '*':
                expand_char = s[i]
                expand = False
            else:
                expand = True
            if not ((i < len(p) and s[i] == p[i]) or (expand and s[i] == expand_char or expand_char == '.')):
                return False
        return True

def test0():
    assert Solution()._Regular_Expression_Matching("aa", "a") == False


def test1():
    assert Solution()._Regular_Expression_Matching("aa", "a*") == True


def test2():
    assert Solution()._Regular_Expression_Matching("ab", ".*") == True


if __name__ == '__main__':
    test0()
    test1()
    test2()
