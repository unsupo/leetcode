# this assumes param has at least one value
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left if type(left) == TreeNode or not left else TreeNode(left)
        self.right = right if type(right) == TreeNode or not right else TreeNode(right)


def createTree(param: List[int], target_value: int = None):
    # root, left, right,
    # left(1 if 1 is not None else 2), right(1 if 1 is not None else 2) , ect
    root = TreeNode(param[0])
    depth = [[root]]  # r, [l,r], [ll,lr,rl,rr], [lll,llr,lrl,lrr,rll,rlr,rrl,rrr]
    k = 0
    x = 1
    target = root
    while x < len(param):
        v = []
        for i in range(len(depth[k])):
            if not depth[k][i]: continue
            if target_value and depth[k][i].val == target_value: target = depth[k][i]
            depth[k][i].left = TreeNode(param[x]) if param[x] is not None else None
            depth[k][i].right = TreeNode(param[x + 1]) if param[x + 1] is not None else None
            v.extend([depth[k][i].left, depth[k][i].right])
            x += 2
        depth.append(v)
        k += 1
    if target_value:
        return root, target
    else:
        return root
