# Diameter of Binary Tree

## Link
https://leetcode.com/problems/diameter-of-binary-tree/

## Where
Leetcode

## Difficulty
Easy

## Description
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

## Solution Main Idea
Recurse to get the max len from left subtree to a leaf in the left subtree, likewise for right subtree. The max len that includes the cur node is the summation of the recursion results. Update max len if that max cur that includes the cur node is more than max len globally.


## Code

```python
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

```
