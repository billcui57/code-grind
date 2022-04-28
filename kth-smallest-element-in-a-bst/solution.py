# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    i = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return None

        left = self.kthSmallest(root.left, k)
        if left is not None:
            return left
        self.i += 1
        if self.i == k:
            return root.val
        right = self.kthSmallest(root.right, k)
        if right is not None:
            return right
