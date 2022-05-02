class Solution(object):
    def _Two_Sum(self, nums, target):
        """
        :type nums: [2,7,11,15]
        :type target: 9
        :rtype: [0,1]
        """
        # Have solution here and remove pass
        pass

        
def test0():
    assert Solution()._Two_Sum([2,7,11,15], 9) == [0,1]

            
def test1():
    assert Solution()._Two_Sum([3,2,4], 6) == [1,2]

            
def test2():
    assert Solution()._Two_Sum([3,3], 6) == [0,1]

            
if __name__ == '__main__':
    test0()
    test1()
    test2()