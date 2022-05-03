class Solution(object):
    def _Median_of_Two_Sorted_Arrays(self, nums1, nums2):
        """
        :type nums1: [1,3]
        :type nums2: [2]
        :rtype: 2.00000
        """
        nums1.extend(nums2)
        sorted(nums1)
        return nums1[len(nums1) // 2] if len(nums1) % 2 == 1 else \
            (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2


def test0():
    assert Solution()._Median_of_Two_Sorted_Arrays([1, 3], [2]) == 2.00000


def test1():
    assert Solution()._Median_of_Two_Sorted_Arrays([1, 2], [3, 4]) == 2.50000


if __name__ == '__main__':
    test0()
    test1()
