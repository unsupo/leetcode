# Definition for a binary tree node.
from typing import List

from util import TreeNode, createTree


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
for i in range(len(output)):
    target_value = input[i][1]
    original, target = createTree(input[i][0].copy(), target_value)
    clone, clone_target = createTree(input[i][0].copy(), target_value)
    r = Solution().getTargetCopy(original, clone, target)
    if r != clone_target:  # TODO how to check that it's from the clone
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
