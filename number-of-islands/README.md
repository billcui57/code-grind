# Number of Islands

## Link

https://leetcode.com/problems/number-of-islands/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

## Solution Main Idea

Component finding. Floodfill (DFS) on unvisited cell that is land and inc island count
