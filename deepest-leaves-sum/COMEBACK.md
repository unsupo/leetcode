this is cool look at the solution

```python

def deepestLeavesSum(self, root: Optional[TreeNode]):
    q = [root]
    while q:
        pre, q = q, [child for p in q for child in [p.left, p.right] if child]
    return sum(node.val for node in pre)

```