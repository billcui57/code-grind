# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        leftMaxDepth = 0
        if root.left:
            leftMaxDepth = self.maxDepth(root.left)

        rightMaxDepth = 0
        if root.right:
            rightMaxDepth = self.maxDepth(root.right)

        return max(leftMaxDepth, rightMaxDepth) + 1
