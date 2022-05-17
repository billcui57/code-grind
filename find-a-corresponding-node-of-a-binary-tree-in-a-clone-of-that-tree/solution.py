# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def is_copy(self, original, cloned):

        if original is None and cloned is None:
            return True

        if original is None:
            return False

        if cloned is None:
            return False

        if original.val != cloned.val:
            return False

        return self.is_copy(original.left, cloned.left) and self.is_copy(
            original.right, cloned.right
        )

    def helper(self, original, cloned, target):

        if original is None:
            return None, False

        assert original.val == cloned.val

        if original.val == target.val:

            is_valid = self.is_copy(original, cloned)

            return cloned, is_valid

        left_result, left_valid = self.helper(original.left, cloned.left, target)

        if left_valid:
            return left_result, True

        right_result, right_valid = self.helper(original.right, cloned.right, target)

        if right_valid:
            return right_result, True

        return None, False

    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:

        result, is_valid = self.helper(original, cloned, target)

        return result
