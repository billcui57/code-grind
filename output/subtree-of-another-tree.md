# Subtree of Another Tree

## Link

https://leetcode.com/problems/subtree-of-another-tree/

## Where

Leetcode

## Difficulty

Easy

## Description

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

## Solution Main Idea

Recurse through tree, find all instances where the root val and subtree val are the same. Recurse on those instances to determine if its the same tree.


## Code

```python
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

```
