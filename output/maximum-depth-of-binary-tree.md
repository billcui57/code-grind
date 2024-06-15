# Maximum Depth of Binary Tree

## Link

https://leetcode.com/problems/maximum-depth-of-binary-tree/

## Where

Leetcode

## Difficulty

Medium

## Description

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Solution Main Idea

Recurse to get maxDepth of left and right subtree, max over both + 1


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        leftMaxDepth = 0
        if root.left:
            leftMaxDepth = self.maxDepth(root.left)

        rightMaxDepth = 0
        if root.right:
            rightMaxDepth = self.maxDepth(root.right)

        return max(leftMaxDepth, rightMaxDepth) + 1

```
