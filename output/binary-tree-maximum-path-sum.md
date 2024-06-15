# Binary Tree Maximum Path Sum

## Link

https://leetcode.com/problems/binary-tree-maximum-path-sum/

## Where

Leetcode

## Difficulty

Hard

## Description

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

## Solution Main Idea

Obtain $pathMax$ from recursing on left and right subtrees, where $pathMax$ represents the maximum path sum of the subtree $a$ that does not include both $a.left$ and $a.right$. Meaning we can construct a longer path from $a$ by adding $root$ to $a$. However at each node we obtain another sum that is the maximum path that can include both $a.left$ and $a.right$ and have that increment a global max.

Observation: if a path goes from one subtree to another subtree, the parent node cannot build on that path.


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    maxPathVal = -inf

    def maxPathSumHelper(self, root):

        if root is None:
            return -inf

        leftPathMax = self.maxPathSumHelper(root.left)
        rightPathMax = self.maxPathSumHelper(root.right)

        localMaxFullPathVal = max(
            leftPathMax + root.val + rightPathMax,
            leftPathMax + root.val,
            rightPathMax + root.val,
            root.val,
        )

        maxPartialPathVal = max(
            leftPathMax + root.val, rightPathMax + root.val, root.val
        )

        self.maxPathVal = max(localMaxFullPathVal, self.maxPathVal)

        return maxPartialPathVal

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxPathSumHelper(root)

        return self.maxPathVal

```
