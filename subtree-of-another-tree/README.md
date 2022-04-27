# Subtree of Another Tree

## Link

https://leetcode.com/problems/subtree-of-another-tree/

## Where

Leetcode

## Difficulty

Easy

## Description

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

## Solution Main Idea

Recurse through tree, find all instances where the root val and subtree val are the same. Recurse on those instances to determine if its the same tree.
