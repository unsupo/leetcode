class Solution(object):
    def _Longest_Substring_Without_Repeating_Characters(self, s):
        """
        :type s: "abcabcbb"
        :rtype: 3
        """
        longest = 0
        seen = set()
        for i in s:
            if i in seen:
                if len(seen) > longest:
                    longest = len(seen)
                seen = set()
            seen.add(i)
        if len(seen) > longest:
            longest = len(seen)
        return longest


def test0():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("abcabcbb") == 3


def test1():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("bbbbb") == 1


def test2():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("pwwkew") == 3


def test3():
    assert Solution()._Longest_Substring_Without_Repeating_Characters(" ") == 1


def test3():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("dvdf") == 3


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
