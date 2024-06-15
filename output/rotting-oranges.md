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


## Code

```python
class Solution:

    def findRotting(self,grid):
        m = len(grid)
        n = len(grid[0])

        rottingPos=set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rottingPos.add((row,col))
        return rottingPos

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        seen = set()

        minDistance = [[-1] * n for i in range(m)] 

        rottingOranges = self.findRotting(grid)
        queue = [(rottingOrangePos, 0) for rottingOrangePos in rottingOranges]
        seen = rottingOranges

        while len(queue) > 0:
            pos,distance = queue.pop(0)
            row,col = pos

            minDistance[row][col] = distance

            neighbours = []
            if row + 1 <= m-1:
                neighbours.append((row+1, col))
            if row - 1 >=0:
                neighbours.append((row -1,col))
            if col + 1 <= n-1:
                neighbours.append((row, col+1))
            if col - 1 >= 0:
                neighbours.append((row, col-1))
            
            for neighbour in neighbours:
                nrow,ncol = neighbour
                if neighbour not in seen and grid[nrow][ncol] != 0:
                    seen.add(neighbour)
                    queue.append((neighbour, distance + 1))
        
        # print(minDistance)
        maxRotDistance = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    if minDistance[row][col] == -1:
                        return -1
                    maxRotDistance = max(maxRotDistance,minDistance[row][col])
        return maxRotDistance

            
            

```
