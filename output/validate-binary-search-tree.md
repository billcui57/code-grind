# Validate Binary Search Tree

## Link

https://leetcode.com/problems/validate-binary-search-tree/

## Where

Leetcode

## Difficulty

Medium

## Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

## Solution Main Idea

Check if left and right subtrees are BST
Check if $root.left.val < root.val && root.val < root.right.val$
Check if the biggest value in left subtree < root.val
Check if the smallest value in right subtree > root.val


## Code

```python
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

```
