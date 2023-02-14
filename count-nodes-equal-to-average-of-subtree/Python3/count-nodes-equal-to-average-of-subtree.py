import timeit
from typing import Optional

from util import TreeNode, createTree


class TreeNodeStat:
    treeNode: TreeNode
    sum: int = 0
    count: int = 0

    def __init__(self, treeNode: TreeNode) -> None:
        self.treeNode = treeNode
        self.sum = treeNode.val
        self.count = 1


class Solution:
    def best_averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, _sum, _cnt, n):
            if node is None:
                return 0, 0, 0
            if node.left is None and node.right is None:
                return node.val, 1, 1
            l_sum, l_n, l_cnt = dfs(node.left, _sum, _cnt, n)
            r_sum, r_n, r_cnt = dfs(node.right, _sum, _cnt, n)
            tmp_sum = (l_sum + r_sum + node.val) // (l_cnt + r_cnt + 1)
            if tmp_sum == node.val:
                return l_sum + r_sum + node.val, l_n + r_n + 1, l_cnt + r_cnt + 1
            return l_sum + r_sum + node.val, l_n + r_n, l_cnt + r_cnt + 1

        # a is total, n is how many matched, and v is how many nodes
        a, n, v = dfs(root, 0, 0, 0)
        return n

    treeNodeStats = []

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.treeNodeStats = []
        self._averageOfSubtree(root)
        cnt = 0
        for i in self.treeNodeStats:
            if i.sum // i.count == i.treeNode.val:
                cnt += 1
        return cnt

    def _averageOfSubtree(self, root: TreeNode) -> TreeNodeStat:
        if root is None: return None
        # this means you've reached a leaf
        if root.left is None and root.right is None:
            # this is always an average of it's subtree
            tns = TreeNodeStat(root)
            self.treeNodeStats.append(tns)
            return tns
        ltns = self._averageOfSubtree(root.left)
        rtns = self._averageOfSubtree(root.right)
        tns = TreeNodeStat(root)
        if ltns:
            tns.count += ltns.count
            tns.sum += ltns.sum
        if rtns:
            tns.count += rtns.count
            tns.sum += rtns.sum
        self.treeNodeStats.append(tns)
        return tns


input = [[4, 8, 5, 0, 1, None, 6], [1]]
output = [5, 1]
for i in range(len(output)):
    r = Solution().best_averageOfSubtree(createTree(input[i]))
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

# print(timeit.timeit(stmt=lambda: Solution().averageOfSubtree(createTree(input[0])), number=1_000_000))
# print(timeit.timeit(stmt=lambda: Solution().best_averageOfSubtree(createTree(input[0])), number=1_000_000))
# 5.958368417006568
# 3.693942333004088