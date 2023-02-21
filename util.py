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
            depth[k][i].left = TreeNode(param[x]) if len(param) > x and param[x] is not None else None
            depth[k][i].right = TreeNode(param[x + 1]) if len(param) > x+1 and param[x + 1] is not None else None
            v.extend([depth[k][i].left, depth[k][i].right])
            x += 2
        depth.append(v)
        k += 1
    if target_value:
        return root, target
    else:
        return root


def createList(root: TreeNode, children_count=2) -> List:
    out = []

    def dfs(root: TreeNode, depth: int):
        if len(out) <= depth:
            out.append([])
        if root is None:
            out[depth].append(None)
            return
        if root.left is None and root.right is None:
            out[depth].append(root.val)
        else:
            out[depth].append(root.val)
        dfs(root.left, depth + 1)
        dfs(root.right, depth + 1)

    dfs(root, 0)

    out = [item for sublist in out for item in sublist]
    last = 0
    for i in range(len(out)):
        if out[i] is not None:
            last = i
    return out[:last+1]


if __name__ == '__main__':
    l = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    t = createTree(l)
    ll = createList(t)
    assert l == ll
