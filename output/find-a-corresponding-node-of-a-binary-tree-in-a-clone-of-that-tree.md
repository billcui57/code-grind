# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

## Link
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

## Where
Leetcode

## Difficulty
Medium

## Description
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

## Solution Main Idea
Find the potential target in original, and then check if original and cloned are the same tree from that root

## Code

```python
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

```
