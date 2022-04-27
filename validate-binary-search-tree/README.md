# Validate Binary Search Tree

## Link

https://leetcode.com/problems/validate-binary-search-tree/

## Where

Leetcode

## Difficulty

Medium

## Description

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

## Solution Main Idea

Check if left and right subtrees are BST
Check if $root.left.val < root.val && root.val < root.right.val$
Check if the biggest value in left subtree < root.val
Check if the smallest value in right subtree > root.val
