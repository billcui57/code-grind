# Lowest Common Ancestor of a Binary Search Tree

## Link

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

## Where

Leetcode

## Difficulty

Easy

## Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Solution Main Idea

A node is a lowest common ancestor of $p$ and $q$ if:

        if p.val < root.val and root.val < q.val

        if q.val < root.val and root.val < p.val

        if p == root and (q.val < root.val or root.val < q.val)

        if q == root and (p.val < root.val or root.val < p.val)

We test for it top down to avoid weird edge cases


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def helper(
        self, root: "TreeNode", smaller: "TreeNode", bigger: "TreeNode"
    ) -> "TreeNode":
        if smaller.val < root.val and bigger.val < root.val:
            return self.helper(root.left, smaller, bigger)
        if smaller.val > root.val and bigger.val > root.val:
            return self.helper(root.right, smaller, bigger)
        if smaller.val <= root.val and bigger.val >= root.val:
            return root

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if p.val > q.val:
            p, q = q, p
        return self.helper(root, p, q)

```
