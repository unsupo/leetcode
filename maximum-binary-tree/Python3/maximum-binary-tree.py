import timeit
from typing import List
from util import TreeNode
from typing import Optional


class Solution:
    def get_max(self, nums):
        m = -1
        mi = -1
        for i in range(len(nums)):
            if nums[i] > m:
                m = nums[i]
                mi = i
        return m, mi

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def recurse(nums, root: TreeNode):
            m, mi = self.get_max(nums)
            root.val = m
            if len(nums[0:mi]) > 0:
                root.left = recurse(nums[0:mi], TreeNode())
            if len(nums[mi + 1:len(nums)]) > 0:
                root.right = recurse(nums[mi + 1:len(nums)], TreeNode())
            return root

        root = TreeNode()
        recurse(nums, root)
        return root

    def best_constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []

        for x in nums:
            n = TreeNode(x)
            # if x > then last element of stack then left of n will be stack.pop()
            while stack and x > stack[-1].val:
                n.left = stack.pop()

            # else n will be right of stack[-1]

            if stack:
                stack[-1].right = n

            stack.append(n)
        return stack[0]


def test(m, silent=False):
    input = [[3, 2, 1, 6, 0, 5], [3, 2, 1]]
    output = [[6, 3, 5, None, 2, 0, None, None, 1], [3, None, 2, None, 1]]
    for i in range(len(output)):
        r = m(input[i])
        if str(r) != str(output[i]):
            raise Exception('Failed: ' + str(input[i]) + ' ---- Got: ' + str(r) + ' !== ' + str(output[i]))
        if not silent:
            print('Passed input: ' + str(input[i]))


test(Solution().best_constructMaximumBinaryTree)

# print(timeit.timeit(stmt=lambda: test(Solution().constructMaximumBinaryTree, True), number=1_000_000))
# print(timeit.timeit(stmt=lambda: test(Solution().best_constructMaximumBinaryTree, True), number=1_000_000))
# 13.148279624991119
# 9.51386283399188
# best is faster