# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import timeit
from typing import Optional

from util import TreeNode, createTree


class Solution:
    sum: int = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:  # or root.val > high or root.val < low:
            return self.sum
        if root.val >= low and root.val <= high:
            self.sum += root.val
        if root.val < high:  # go right
            self.rangeSumBST(root.right, low, high)
        if root.val > low:  # go left
            self.rangeSumBST(root.left, low, high)
        return self.sum

    def best_rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans


input = [[[10, 5, 15, 3, 7, None, 18], 7, 15], [[10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10]]
output = [32, 23]
for i in range(len(output)):
    r = Solution().rangeSumBST(createTree(input[i][0]), *input[i][1:])
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

# tree = createTree(input[0][0])
# print(timeit.timeit(stmt=lambda: Solution().rangeSumBST(tree, *input[0][1:]), number=1_000_000))
# print(timeit.timeit(stmt=lambda: Solution().best_rangeSumBST(tree, *input[0][1:]), number=1_000_000))
# 1.1553101250901818
# 1.0342518339166418