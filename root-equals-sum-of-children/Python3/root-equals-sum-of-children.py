# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None): # TODO this was commented out
        self.val = val
        self.left = left if type(left) == TreeNode or not left else TreeNode(left)
        self.right = right if type(right) == TreeNode or not right else TreeNode(right)
from typing import Optional # TODO this wasn't imported


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == sum([root.left.val, root.right.val])


input = [[10, 4, 6], [5, 3, 1]]
output = [True, False]
for i in range(len(output)):
    r = Solution().checkTree(TreeNode(*input[i])) # TODO input needs to be Optional[TreeNode]
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
