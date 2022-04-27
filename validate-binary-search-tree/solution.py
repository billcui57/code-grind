# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root):
        if root is None:
            return None, None, True

        if not root.left and not root.right:
            return root.val, root.val, True

        leftSmallest, leftBiggest, leftIsValid = self.helper(root.left)
        rightSmallest, rightBiggest, rightIsValid = self.helper(root.right)

        isValid = True

        if not leftIsValid or not rightIsValid:
            isValid = False

        if leftBiggest:
            isValid = isValid and leftBiggest < root.val

        if rightSmallest:
            isValid = isValid and root.val < rightSmallest

        if root.left:
            isValid = isValid and root.left.val < root.val

        if root.right:
            isValid = isValid and root.val < root.right.val

        return leftSmallest, rightBiggest, isValid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        smallest, biggest, isValid = self.helper(root)
        return isValid
