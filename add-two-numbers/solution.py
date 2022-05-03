class Solution(object):
    def _Add_Two_Numbers(self, l1, l2):
        """
        :type l1: [2,4,3]
        :type l2: [5,6,4]
        :rtype: [7,0,8]
        """
        # l3 = l1[::-1]
        # l4 = l2[::-1]
        l5 = []
        r = 0
        for i in range(len(l1)):
            v = l1[i]+l2[2]
            if v//10 >= 1:
                r = v//10
                v = v%10
            else:
                v += r
                r = 0
            l5.append(v)

def test0():
    assert Solution()._Add_Two_Numbers([2,4,3], [5,6,4]) == [7,0,8]

            
def test1():
    assert Solution()._Add_Two_Numbers([0], [0]) == [0]

            
def test2():
    assert Solution()._Add_Two_Numbers([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1]

            
if __name__ == '__main__':
    test0()
    test1()
    test2()
