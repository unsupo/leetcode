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
        g = ""  # i'll assume i can't split here since i can't use re
        i = 0
        while i < len(p):
            if i + 1 < len(p) and p[i + 1] == "*":
                if g:
                    groups.append(g)
                if not groups or (groups[-1] != '.*' and p[i:i + 2] != groups[-1]):  # duplicates .*.*a* == .*
                    groups.append(p[i:i + 2])
                g = ""
                i += 1
            else:
                g += p[i]
            i += 1
        if g: groups.append(g)
        # now i have groups like asdf, a*, b*, .* ect
        # order matters, find the first group if not then return false
        groups_index = 0
        str_index = 0
        while str_index < len(s):
            expand = False
            expand_char = ""
            if groups_index >= len(groups):
                return False
            group = groups[groups_index]
            if len(group) == 2 and '*' == group[1]:  # if this fails then above while loop failed
                expand = True
                expand_char = group[0]
            found = False
            for group_index in range(len(group)):
                if expand:
                    if expand_char == '.' or s[str_index] == expand_char:
                        # if it's a dot then check the next non group to see if it matches
                        if expand_char == '.' and groups_index + 1 < len(groups):
                            # i can assume next group is not a .* or else above while loop failed
                            found_match = True
                            tmp_str_index = str_index
                            for nxt_group_char in groups[groups_index + 1]:
                                if nxt_group_char != s[tmp_str_index]:
                                    found_match = False
                                    break
                                tmp_str_index += 1
                            # if found_match is True then the next group was found so move on from that and dot match
                            if found_match:
                                str_index = tmp_str_index
                                groups_index += 2
                        found = True  # if it matches then stay on this group
                    else:
                        str_index -= 1
                    break
                elif group[group_index] != s[str_index]:
                    return False
            if not found:
                groups_index += 1
            str_index += 1
        if str_index >= len(s):
            return True
        return False


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


def test4():
    assert Solution()._Regular_Expression_Matching("drrraomnklbbbbc", "dr*a.*.*b*b*b*c") == True


def tester(a, b, r):
    assert Solution()._Regular_Expression_Matching(a, b) == r


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    # [tester(*i) for i in [
    #     ["", "r*", True],
    #     ["rasdfew", "r.*", True],
    #     ["adsfdsfa", "a.*a", True],
    #     ["adsfdsf", "a.*a", False],
    #     ["dsfdsfa", "a.*a", False],
    #     ["adfsjlkadfsklj", "a.*a.*", True],
    #     ["dfsjlkadfsklj", "a.*a.*", False],
    #     ["adfsjlkdfsklj", "a.*a.*", False]
    # ]]
