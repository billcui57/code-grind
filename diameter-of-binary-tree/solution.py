# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    maxLen = 0

    def helper(self, root):
        if root == None:
            return -1

        left = self.helper(root.left)
        right = self.helper(root.right)

        length = 1 + left + 1 + right

        self.maxLen = max(length, self.maxLen)

        return max(1 + left, 1 + right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)

        return self.maxLen
