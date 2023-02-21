import timeit

from util import TreeNode, createTree


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, parent_val, grandparent_val):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if grandparent_val and grandparent_val % 2 == 0 else 0
            s = dfs(node.left, node.val, parent_val)
            s += dfs(node.right, node.val, parent_val)
            return node.val + s if grandparent_val and grandparent_val % 2 == 0 else s
        return dfs(root, None, None)

    # the best solution on leetcode isn't better, must have just been lucky
    def better_sumEvenGrandparent(self, root: TreeNode) -> int:
        def trans(root, grand_parent, parent_value):
            if root == None:
                return 0
            left = trans(root.left, parent_value, root.val)
            if grand_parent % 2 == 0:
                left += root.val
            right = trans(root.right, parent_value, root.val)
            return left + right
        return trans(root, 1, 1)

input = [[6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], [1]]
output = [18, 0]
for i in range(len(output)):
    r = Solution().sumEvenGrandparent(createTree(input[i]))
    if str(r) != str(output[i]):
        raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
    print('Passed input: ' + str(input[i]))

tree = createTree(input[0])
print(timeit.timeit(stmt=lambda: Solution().sumEvenGrandparent(tree), number=1_000_000))
print(timeit.timeit(stmt=lambda: Solution().better_sumEvenGrandparent(tree), number=1_000_000))