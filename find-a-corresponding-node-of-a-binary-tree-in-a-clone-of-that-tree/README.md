# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

## Link
https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

## Where
Leetcode

## Difficulty
Medium

## Description
Given two binary trees original and cloned and given a reference to a node target in the original tree.

The cloned tree is a copy of the original tree.

Return a reference to the same node in the cloned tree.

Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.

## Solution Main Idea
Find the potential target in original, and then check if original and cloned are the same tree from that root