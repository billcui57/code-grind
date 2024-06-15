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


## Code

```python
class Solution:
    def floodFill(self, cell, grid, visited):

        visited.add(cell)

        y = cell[0]
        x = cell[1]
        height = len(grid)
        width = len(grid[0])

        neighbours = []

        if x - 1 > -1 and grid[y][x - 1] == "1":
            neighbours.append((y, x - 1))
        if x + 1 < width and grid[y][x + 1] == "1":
            neighbours.append((y, x + 1))
        if y - 1 > -1 and grid[y - 1][x] == "1":
            neighbours.append((y - 1, x))
        if y + 1 < height and grid[y + 1][x] == "1":
            neighbours.append((y + 1, x))

        for neighbour in neighbours:
            if neighbour not in visited:
                self.floodFill(neighbour, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        numIslands = 0

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.floodFill((row, col), grid, visited)
                    numIslands += 1

        return numIslands

```
