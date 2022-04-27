# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    maxPathVal = -inf

    def maxPathSumHelper(self, root):

        if root is None:
            return -inf

        leftPathMax = self.maxPathSumHelper(root.left)
        rightPathMax = self.maxPathSumHelper(root.right)

        localMaxFullPathVal = max(
            leftPathMax + root.val + rightPathMax,
            leftPathMax + root.val,
            rightPathMax + root.val,
            root.val,
        )

        maxPartialPathVal = max(
            leftPathMax + root.val, rightPathMax + root.val, root.val
        )

        self.maxPathVal = max(localMaxFullPathVal, self.maxPathVal)

        return maxPartialPathVal

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxPathSumHelper(root)

        return self.maxPathVal
