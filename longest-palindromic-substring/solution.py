class Solution(object):
    memoize = {}
    def _Longest_Palindromic_Substring(self, s):
        """
        :type s: "babad"
        :rtype: "bab"
        """
        # greedy tree search
        # one path cuts off left char
        # one path cuts off right char
        # thrid path splits in half
        if self.is_palandrome(s):
            return s
        if s in self.memoize:
            return self.memoize[s]
        a = self._Longest_Palindromic_Substring(s[1:])
        b = self._Longest_Palindromic_Substring(s[:-1])
        c = self._Longest_Palindromic_Substring(s[1:-1])
        d = self._Longest_Palindromic_Substring(s[len(s) // 2:])
        e = self._Longest_Palindromic_Substring(s[:-len(s) // 2])
        longest = sorted([a, b, c, d, e], key=lambda x: len(x), reverse=True)[0]
        self.memoize[s] = longest
        return longest

    def is_palandrome(self, s):
        return s == s[::-1]

    def attempt1(self, s):  # doesn't work if answer not in middle, no exmaple was given like this
        if s == s[::-1]:
            return s
        l = len(s)
        for i in range(1, l):
            if s[i:l] == s[i:l][::-1]:
                return s[i:l]
            if s[:-i] == s[:-i][::-1]:
                return s[:-i]
            if len(s[i:-i]) > 1 and s[i:-i] == s[i:-i][::-1]:
                return s[i:-i]
        return s[0]


def test0():
    v = Solution()._Longest_Palindromic_Substring("babad")
    assert v == "bab" or v == "aba"


def test1():
    assert Solution()._Longest_Palindromic_Substring("cbbd") == "bb"


def test2():
    assert Solution()._Longest_Palindromic_Substring("aacabdkacaa") == "aca"


def test3():
    assert Solution()._Longest_Palindromic_Substring("xaabacxcabaaxcabaax") == "xaabacxcabaax"


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
