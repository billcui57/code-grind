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
