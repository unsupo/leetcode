from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def get_list(self):
        def it(n: ListNode):
            while n:
                yield n
                n = n.next

        return [i.val for i in it(self)]

    def __eq__(self, other):
        return self.get_list() == other.get_list()


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        curr = head
        while curr.next:
            if curr.val == 0:
                l.append([])
            else:
                l[-1].append(curr.val)
            curr = curr.next
        r = ListNode(sum(l[0]))
        n = r
        for i in l[1:]:
            n.next = ListNode(sum(i))
            n = n.next
        return r

    def betterMergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = head
        ptr2 = head.next
        s = 0
        while ptr2:
            if ptr2.val == 0: # override the existing list node with new solution
                ptr1 = ptr1.next
                ptr1.val = s
                s = 0
            else:
                s += ptr2.val
            ptr2 = ptr2.next
        ptr1.next = None
        return head.next


def create_listNode(l: List[int]) -> Optional[ListNode]:
    root = ListNode(l[0])
    n = root
    for i in l[1:]:
        n.next = ListNode(i)
        n = n.next
    return root


input = [[0, 3, 1, 0, 4, 5, 2, 0], [0, 1, 0, 3, 0, 2, 2, 0]]
output = [[4, 11], [1, 3, 4]]
for i in range(len(output)):
    r = Solution().betterMergeNodes(create_listNode(input[i]))
    o = create_listNode(output[i])
    if r != o:
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
