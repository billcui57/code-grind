# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):

        if node == None:
            return (True, 0)

        left = self.helper(node.left)
        right = self.helper(node.right)

        if left[0] == False or right[0] == False:
            return (False, None)

        if abs(left[1] - right[1]) > 1:
            return (False, None)

        return (True, 1 + max(left[1], right[1]))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.helper(root)[0]
