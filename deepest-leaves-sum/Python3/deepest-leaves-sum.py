from typing import Optional
from util import TreeNode, createTree


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


input = [[1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8],
         [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]]
output = [15, 19]
for i in range(len(output)):
    r = Solution().deepestLeavesSum(createTree(input[i]))
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))
