from memory_profiler import profile

from functools import wraps
from time import time


class Solution(object):
    memoize = {}
    def _Longest_Palindromic_Substring(self, s):
        pass

    def attempt2(self, s):
        """
        :type s: "babad"
        :rtype: "bab"
        """
        rev = s[::-1]
        if s == rev:
            return s
        if s in self.memoize:
            return self.memoize[s]
        if rev in self.memoize:
            return self.memoize[rev]
        a = self.attempt2(s[1:])
        b = self.attempt2(s[:-1])
        longest = a if len(a) > len(b) else b #sorted([a, b], key=lambda x: len(x), reverse=True)[0]
        # if len(s) != 1: # 224.3 vs 224.6
        #     self.memoize[s] = longest
        self.memoize[s] = longest
        return longest

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
@profile
def test6():
    assert Solution().attempt2(
        "zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir") == "gykrkyg"


@timing
# @profile
def test7():
    assert Solution()._Longest_Palindromic_Substring(
        "iptmykvjanwiihepqhzupneckpzomgvzmyoybzfynybpfybngttozprjbupciuinpzryritfmyxyppxigitnemanreexcpwscvcwddnfjswgprabdggbgcillisyoskdodzlpbltefiz") == "illi"


if __name__ == '__main__':
    # test0()
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    test6()
    # test7()
