# Rotting Oranges

## Link

https://leetcode.com/problems/rotting-oranges/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

## Solution Main Idea

Use BFS with all rotten oranges as start nodes. Obtain distance matrix of all nodes from rotten oranges. Return max distance among all oranges. But return -1 if there are oranges that cant be rotted
