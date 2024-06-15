# Lowest Common Ancestor of a Binary Tree III

## Link

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is below:

````class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}```
According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."



## Solution Main Idea
Traverse to parent. Single path to root node. Return point of intersection for both nodes.
````


## Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def helper(self,node,seen,result):
        if node.val in seen:
            result.append(node)
            return
        seen.add(node.val)
        if node.parent is not None:
            self.helper(node.parent, seen,result)

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        seen =set()
        result = []
        self.helper(p, seen, result)
        self.helper(q,seen,result)
        return result.pop()
```
