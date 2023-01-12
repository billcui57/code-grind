# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def helper(
        self, root: "TreeNode", smaller: "TreeNode", bigger: "TreeNode"
    ) -> "TreeNode":
        if smaller.val < root.val and bigger.val < root.val:
            return self.helper(root.left, smaller, bigger)
        if smaller.val > root.val and bigger.val > root.val:
            return self.helper(root.right, smaller, bigger)
        if smaller.val <= root.val and bigger.val >= root.val:
            return root

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val > q.val:
            p, q = q, p
        return self.helper(root, p, q)
