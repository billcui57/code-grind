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


## Code

```python
class Solution:



    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[inf] * n for i in range(m)]

        queue = []
        seen= set()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col,0))
                    result[row][col] = 0
                    seen.add((row,col))
        
        
        while len(queue) > 0:
            row,col,distFromZero = queue.pop(0)
       
            result[row][col] = distFromZero

            neighbours = []

            if row - 1 >= 0:
                neighbours.append((row-1,col))
            if row + 1 <= m-1:
                neighbours.append((row+1, col))
            if col - 1 >= 0:
                neighbours.append((row, col-1))
            if col + 1 <= n-1:
                neighbours.append((row, col+1))
            
           
            for neighbour in neighbours:
                nrow,ncol = neighbour
                if (nrow,ncol) not in seen:
                    result[nrow][ncol] = distFromZero + 1
                    queue.append((nrow, ncol,distFromZero+1))
                    seen.add((nrow,ncol))
        return result

        
```
