# Lowest Common Ancestor of a Binary Tree

## Link

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Solution Main Idea

Recurse on left and right, keep track of which nodes are found in which subtree. Propagate back up


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def helper(self,root,p,q):
        if root is None:
            return None, False, False
        
        leftResult,leftPFound,leftQFound = self.helper(root.left,p,q)
        rightResult, rightPFound, rightQFound = self.helper(root.right,p,q)

        if leftResult:
            return leftResult, True, True
        if rightResult:
            return rightResult, True,True

        containsP = (root.val == p.val) or leftPFound or rightPFound
        containsQ = (root.val == q.val) or leftQFound or rightQFound

        if containsP and containsQ:
            return root, True, True
        
        if root.val == p.val:
            return None, True, False
        if root.val ==q.val :
            return None, False, True

        return None, containsP,containsQ
    

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result,pfound,qfound = self.helper(root,p,q)
        return result
        
```
