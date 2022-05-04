class Solution(object):
    def _Regular_Expression_Matching(self, s, p):
        """
        :type s: "aa"
        :type p: "a"
        :rtype: false
        """
        if p == '.*': return True
        if not p or p[0] == "*": return False
        # attempt to split by * call these groups
        groups = []
        g = ""
        for i in p:
            if i == "*":
                g += "*"
                groups.append(g)
                g = ""
            g += p[i]
        # now i have groups like asdf, a*, b*, .* ect
        # order matters, find the first group if not then return false
        # if true move to the next group

    def attempt1(self, s, p):
        if p == '.*': return True
        if not p: return False
        expand = False
        expand_char = ""
        j = 0
        r = p[0]
        for i in range(len(s)):
            if r != '.' and s[i] != r:  # need to also look to the next character here but only if expand
                if r == '*':
                    r = expand_char
                    expand = True
                    j += 1
                else:
                    r = p[j]
                    expand_char = r
            if r != '.' and s[i] != r:
                return False
            if not expand:
                j += 1
                expand_char = r
                if j >= len(p):
                    return False
                r = p[j]
        return True


def test0():
    assert Solution()._Regular_Expression_Matching("aa", "a") == False


def test1():
    assert Solution()._Regular_Expression_Matching("aa", "a*") == True


def test2():
    assert Solution()._Regular_Expression_Matching("ab", ".*") == True


def test3():
    assert Solution()._Regular_Expression_Matching("rrraaaa", "r*a*") == True


def tester(a, b, r):
    assert Solution()._Regular_Expression_Matching(a, b) == r


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    [tester(*i) for i in [
        ["", "r*", True],
        ["rasdfew", "r.*", True],
        ["adsfdsfa", "a.*a", True],
        ["adsfdsf", "a.*a", False],
        ["dsfdsfa", "a.*a", False],
        ["adfsjlkadfsklj", "a.*a.*", True],
        ["dfsjlkadfsklj", "a.*a.*", False],
        ["adfsjlkdfsklj", "a.*a.*", False]
    ]]
