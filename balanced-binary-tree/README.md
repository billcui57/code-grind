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
