class Solution(object):
    def _Longest_Palindromic_Substring(self, s):
        """
        :type s: "babad"
        :rtype: "bab"
        """
        if s == s[::-1]:
            return s
        l = len(s)
        for i in range(1, l):
            if s[i:l] == s[i:l][::-1]:
                return s[i:l]
            if s[:-i] == s[:-i][::-1]:
                return s[:-i]
            if s[i:-i] == s[i:-i][::-1]:
                return s[i:-i]
        return None


def test0():
    v = Solution()._Longest_Palindromic_Substring("babad")
    assert v == "bab" or v == "aba"


def test1():
    assert Solution()._Longest_Palindromic_Substring("cbbd") == "bb"


def test2():
    assert Solution()._Longest_Palindromic_Substring("cbbd") == "bb"


if __name__ == '__main__':
    test0()
    test1()
