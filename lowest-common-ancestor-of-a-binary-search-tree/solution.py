# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        if p.val < root.val and root.val < q.val:
            return root

        if q.val < root.val and root.val < p.val:
            return root

        if p == root and (q.val < root.val or root.val < q.val):
            return root

        if q == root and (p.val < root.val or root.val < p.val):
            return root

        left = self.lowestCommonAncestor(root.left, p, q)

        if left is not None:
            return left

        right = self.lowestCommonAncestor(root.right, p, q)

        if right is not None:
            return right

        return None
