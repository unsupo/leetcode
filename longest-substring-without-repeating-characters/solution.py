class Solution(object):
    def _Longest_Substring_Without_Repeating_Characters(self, s):
        """
        :type s: "abcabcbb"
        :rtype: 3
        """
        longest = 0
        seen = []
        done = []
        for i in s:
            s = set()
            seen.append(s)
            for j in seen:
                if i in j:
                    done.append(j)
                    seen.remove(j)
            s.add(i)
        done.extend(seen)
        for i in done:
            if len(i) > longest:
                longest = len(i)
        return longest


def test0():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("abcabcbb") == 3


def test1():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("bbbbb") == 1


def test2():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("pwwkew") == 3


def test3():
    assert Solution()._Longest_Substring_Without_Repeating_Characters(" ") == 1


def test4():
    assert Solution()._Longest_Substring_Without_Repeating_Characters("dvdf") == 3


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
