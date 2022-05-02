class Solution(object):
    def _Two_Sum(self, nums, target):
        """
        :type nums: [3,3]
        :type target: 6
        :rtype: [0,1]
        """
        # Have solution here
        pass

def test0():
    assert Solution()._Two_Sum([3,3], 6) == [0,1]

def test1():
    assert Solution()._Two_Sum([3,3], 6) == [1,2]

def test2():
    assert Solution()._Two_Sum([3,3], 6) == [0,1]

if 'name' == __main__:
    test0()
    test1()
    test2()
