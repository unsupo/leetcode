from memory_profiler import profile

from functools import wraps
from time import time

"""
babad
    baba
        bab
        aba
    abab
        aba
        bab

"""


class Solution(object):
    memoize = {}

    def _Longest_Palindromic_Substring(self, s):
        # assume 1 exists then move up to two until you don't find a palendrone
        if self.is_palindrone(s):  # .97
            return s
        palendrone = s[0]
        # palendrone length
        for i in range(2, len(s) - 1):  # start at length 2
            for j in range(len(s) - i):
                if self.is_palindrone(s[j:i + j]):
                    palendrone = s[j:i + j] if len(s[j:i + j]) > len(palendrone) else palendrone
                    break  # break here, no need to find all of this length
        return palendrone

    def attempt2(self, s):
        """
        :type s: "babad"
        :rtype: "bab"
        """
        if self.is_palindrone(s):  # .97
            return s
        if s in self.memoize:
            return self.memoize[s]
        a = self.attempt2(s[1:])
        b = self.attempt2(s[:-1])
        longest = a if len(a) > len(b) else b  # sorted([a, b], key=lambda x: len(x), reverse=True)[0]
        self.memoize[s] = longest
        return longest

    def is_palindrone(self, s):
        l = len(s)
        for i in range(l // 2):
            if s[i] != s[l - i - 1]:
                return False
        return True

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


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
              (f.__name__, args, kw, te - ts))
        return result

    return wrap


@timing
def test0():
    v = Solution()._Longest_Palindromic_Substring("babad")
    assert v == "bab" or v == "aba"


@timing
def test1():
    assert Solution()._Longest_Palindromic_Substring("cbbd") == "bb"


@timing
def test2():
    assert Solution()._Longest_Palindromic_Substring("aacabdkacaa") == "aca"


@timing
def test3():
    assert Solution()._Longest_Palindromic_Substring("xaabacxcabaaxcabaax") == "xaabacxcabaax"


@timing
def test4():
    assert Solution()._Longest_Palindromic_Substring(
        "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy") == "fklkf"


@timing
def test5():
    assert Solution()._Longest_Palindromic_Substring(
        "jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel") == "sknks"


@timing
# @profile
def test6():
    assert Solution()._Longest_Palindromic_Substring(
        "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir") == "gykrkyg"


@timing
# @profile
def test7():
    assert Solution()._Longest_Palindromic_Substring(
        "iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz") == "illi"


@timing
def test8():
    assert Solution()._Longest_Palindromic_Substring("abb") == "bb"


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()  # 1.17
    test7()
    test8()
