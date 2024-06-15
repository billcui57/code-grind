# Balanced Binary Tree

## Link
https://leetcode.com/problems/balanced-binary-tree/

## Where
Leetcode

## Difficulty
Medium

## Description
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.


## Solution Main Idea
Recurse on left and right tree, returning both the height of the subtree as well as if the subtree is a balanced tree.
If subtree isnt a balanced tree then return not balanced. Otherwise, the current tree is balanced if abs(left[1] - right[1]) <=1.>


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node):

        if node == None:
            return (True, 0)

        left = self.helper(node.left)
        right = self.helper(node.right)

        if left[0] == False or right[0] == False:
            return (False, None)

        if abs(left[1] - right[1]) > 1:
            return (False, None)

        return (True, 1 + max(left[1], right[1]))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        return self.helper(root)[0]

```
