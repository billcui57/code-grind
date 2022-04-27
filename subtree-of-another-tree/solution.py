# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, root, subRoot):

        if root is None and subRoot is None:
            return True

        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
                root.right, subRoot.right
            )

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        isST = False

        if root and subRoot and root.val == subRoot.val:
            isST = isST or self.isSameTree(root, subRoot)

        if root:
            isST = (
                isST
                or self.isSubtree(root.left, subRoot)
                or self.isSubtree(root.right, subRoot)
            )

        return isST
