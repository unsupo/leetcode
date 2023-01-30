# Definition for a binary tree node.
from typing import List


class TreeNode:  # TODO this was commented out
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
    #     # it stands for iterators are basically lists that don't store all values but just current
    #     # this is ~2x faster but similar in memory to solution below
    #     def it(node):
    #         if node:
    #             yield node  # yield is not return it is the value of current
    #             yield from it(node.left)  # then when next is called it goes to the next yield
    #             yield from it(node.right)  # yield from is: for i in it(node.right): yield i
    #
    #     # zip combines o and c like => ((o1,c1),(o2,c2),(on,cn)) length is min(o,c), zip will do one iterator at a time
    #     for n1, n2 in zip(it(original), it(cloned)):
    #         if n1 == target:
    #             return n2
    # # why can't i just search the cloned tree for target and ignore original
    # # still not sure why this doesn't work
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # can basically convert tree to list and keep track of location that way
        if cloned.val == target: return cloned
        depth = [[cloned]] # space is O(d) d=depth of tree
        d = 0
        while True: # would have to modify to if comparing nodes (repeated values)
            v=[] # we only use original if we compare node not value
            for i in range(len(depth[d])): # time is O(n) n=number of nodes
                if not depth[d][i]: continue
                if depth[d][i].val == target.val:
                    return depth[d][i]
                v.extend([depth[d][i].left, depth[d][i].right])
            d += 1
            depth.append(v)


# TODO these null's should be None
# TODO these sub arrays weren't created
input = [[[7, 4, 3, None, None, 6, 19], 3], [[7], 7], [[8, None, 6, None, 5, None, 4, None, 3, None, 2, None, 1], 4]]
output = [3, 7, 4]


# TODO this wasn't included
# this assumes param has at least one value
def createTree(param: List[int], target_value: int):
    # root, left, right,
    # left(1 if 1 is not None else 2), right(1 if 1 is not None else 2) , ect
    root = TreeNode(param[0])
    depth = [[root]]  # r, [l,r], [ll,lr,rl,rr], [lll,llr,lrl,lrr,rll,rlr,rrl,rrr]
    k = 0
    x = 1
    target=root
    while x < len(param):
        v = []
        for i in range(len(depth[k])):
            if not depth[k][i]: continue
            if depth[k][i].val == target_value: target = depth[k][i]
            depth[k][i].left = TreeNode(param[x]) if param[x] else None
            depth[k][i].right = TreeNode(param[x + 1]) if param[x + 1] else None
            v.extend([depth[k][i].left, depth[k][i].right])
            x += 2
        depth.append(v)
        k += 1
    return root, target


for i in range(len(output)):
    target_value = input[i][1]
    original, target = createTree(input[i][0].copy(), target_value)
    clone, clone_target = createTree(input[i][0].copy(), target_value)
    r = Solution().getTargetCopy(original, clone, target)
    if r != clone_target:  # TODO how to check that it's from the clone
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
