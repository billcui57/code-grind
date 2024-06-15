# Count Univalue Subtrees

## Link

https://leetcode.com/problems/count-univalue-subtrees/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given the root of a binary tree, return the number of uni-value
subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

## Solution Main Idea

Recurse and return tuple of if child nodes are unival and their values


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, result):
        if node is None:
            return False, None

        if node.left is None and node.right is None:
            result[0] += 1
            return True, node.val
        
        leftUni = False
        rightUni = False
        leftVal = None
        rightVal = None
        if node.left:
            leftUni,leftVal = self.helper(node.left,result)
        if node.right:
            rightUni, rightVal = self.helper(node.right,result)
        
        if (not node.left or (leftUni and leftVal == node.val)) and (not node.right or (rightUni and rightVal == node.val)):
            result[0]+=1
            return True, node.val
        return False, node.val
        

    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = [0]
        self.helper(root, result)
        return result[0]

```
