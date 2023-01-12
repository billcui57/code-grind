# 01 Matrix

## Link

https://leetcode.com/problems/01-matrix/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

## Solution Main Idea

Use BFS. Add all zeros cells to the queue first. Add neighbours to the queue. This ensures that all neighbours popped from front of queue have distance <= distance of neighbours popped later on. Therefore we only need a simple seen set. Add distance to a result matrix for each popped neighbour.
We can think of the algo as dropping n many beads of water into bed of water simultaneously. Where the ripples meet are where its equal distance from the source.
