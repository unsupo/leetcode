# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def to_list_node(arr):
        rarr = arr[::-1]
        ln = ListNode(rarr[0])
        for i in rarr[1:]:
            ln = ListNode(i, ln)
        return ln


class Solution(object):
    def _Add_Two_Numbers_list(self, l1, l2):
        """
        :type l1: [2,4,3]
        :type l2: [5,6,4]
        :rtype: [7,0,8]
        """
        l5 = []
        bigger = l1
        smaller = l2
        if len(l1) < len(l2):
            bigger = l2
            smaller = l1
        r = 0
        for i in range(len(bigger)):
            if i >= len(smaller):
                v = bigger[i]
            else:
                v = l1[i] + l2[i]
            if r > 0:
                v += r
                if v < 10:
                    r = 0
            if v // 10 >= 1:
                r = v // 10
                v = v % 10
            l5.append(v)
        if r > 0:
            l5.append(r)
        return l5

    def _Add_Two_Numbers(self, l1, l2):
        l3 = l1
        l4 = None
        r = 0
        while l3.next:
            v = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
            if r > 0:
                v += r
                if v < 10:
                    r = 0
            if v // 10 >= 1:
                r = v // 10
                v = v % 10
            l4 = ListNode(v, l4)
            if not l3.next: l3 = l2
        if r > 0:
            l4 = ListNode(r, l4)
        return l4

def test0():
    assert Solution()._Add_Two_Numbers(ListNode.to_list_node([2, 4, 3]),
                                       ListNode.to_list_node([5, 6, 4])) == ListNode.to_list_node([7, 0, 8])


def test1():
    assert Solution()._Add_Two_Numbers(ListNode.to_list_node([0]), ListNode.to_list_node([0])) == ListNode.to_list_node(
        [0])


def test2():
    assert Solution()._Add_Two_Numbers(ListNode.to_list_node([9, 9, 9, 9, 9, 9, 9]),
                                       ListNode.to_list_node([9, 9, 9, 9])) == ListNode.to_list_node(
        [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == '__main__':
    test0()
    test1()
    test2()
