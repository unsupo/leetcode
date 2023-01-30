from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]):
        q = [root]
        while q:
            pre, q = q, [child for p in q for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)

    # def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    #     def it(node: TreeNode, depth: int = 0):
    #         if node:
    #             yield node, depth
    #             yield from it(node.left, depth+1)
    #             yield from it(node.right, depth+1)
    #     node_depth = {}
    #     max_depth = 0
    #     for node, depth in it(root):
    #         max_depth = max(max_depth, depth)
    #         if depth not in node_depth:
    #             node_depth[depth]=[]
    #         node_depth[depth].append(node.val)
    #     return sum(node_depth[max_depth])


# TODO this wasn't included
# this assumes param has at least one value
def createTree(param: List[int]):
    # root, left, right,
    # left(1 if 1 is not None else 2), right(1 if 1 is not None else 2) , ect
    root = TreeNode(param[0])
    depth = [[root]]  # r, [l,r], [ll,lr,rl,rr], [lll,llr,lrl,lrr,rll,rlr,rrl,rrr]
    k = 0
    x = 1
    while x < len(param):
        v = []
        for i in range(len(depth[k])):
            if not depth[k][i]: continue
            depth[k][i].left = TreeNode(param[x]) if param[x] else None
            depth[k][i].right = TreeNode(param[x + 1]) if param[x + 1] else None
            v.extend([depth[k][i].left, depth[k][i].right])
            x += 2
        depth.append(v)
        k += 1
    return root


input = [[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8],
         [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]]
output = [15, 19]
for i in range(len(output)):
    r = Solution().deepestLeavesSum(createTree(input[i]))
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
