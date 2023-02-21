# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import timeit

from util import TreeNode, createTree, createList


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(_root: TreeNode, s: int):
            if _root is None:
                return s, s
            if _root.left is None and _root.right is None:
                _root.val += s
                return _root.val, _root.val
            r, s = dfs(_root.right, s)
            _root.val += s
            r, s = dfs(_root.left, _root.val)
            return _root.val, max(_root.val, s)

        dfs(root, 0)

        return root

    val: int = 0
    def best_bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.best_bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.best_bstToGst(root.left)
        return root


input = [[4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8], [0, None, 1], [3, 2, 4, 1]]
output = [[30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8], [1, None, 1], [7, 9, 4, 10]]
for i in range(len(output)):
    r = Solution().best_bstToGst(createTree(input[i]))
    out = str(createList(r))
    if out != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + out + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

tree = createTree(input[0])
print(timeit.timeit(stmt=lambda: Solution().bstToGst(tree), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().best_bstToGst(tree), number=1_000_000))
# roughly produce the same timings