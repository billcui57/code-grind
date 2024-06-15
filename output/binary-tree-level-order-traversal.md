# Binary Tree Level Order Traversal

## Link

https://leetcode.com/problems/binary-tree-level-order-traversal/

## Where

Leetcode

## Difficulty

Medium

## Description

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

## Solution Main Idea

BFS while keep tracking track of the node's distance away from root. Insert to list at index $distance$


## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []

        if root:
            queue.append((root, 0))

        result = []

        while len(queue) > 0:

            node, level = queue.pop(0)

            if level >= len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

```
