class Solution(object):
    def _Median_of_Two_Sorted_Arrays(self, nums1, nums2):
        """
        :type nums1: [1,3]
        :type nums2: [2]
        :rtype: 2.00000
        """
        nums3 = nums1.extend(nums2)
        return nums3[len(nums3//2)] if len(nums3)%2==1 else (nums3[len(nums3//2)]+nums3[len(nums3//2)-1])/2

        
def test0():
    assert Solution()._Median_of_Two_Sorted_Arrays([1,3], [2]) == 2.00000

            
def test1():
    assert Solution()._Median_of_Two_Sorted_Arrays([1,2], [3,4]) == 2.50000

            
if __name__ == '__main__':
    test0()
    test1()
