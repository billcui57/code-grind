# Pacific Atlantic Water Flow

## Link

https://leetcode.com/problems/pacific-atlantic-water-flow/

## Where

Leetcode

## Difficulty

Medium

## Description

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

## Solution Main Idea

Use floodfill (BFS or DFS). Instead of solving "which cells can flow to the ocean", think about "which cells can the ocean flow to if water can flow upwards". Cells adjacent to ocean are coloured. Colour all cells that are adjacent to colour cells, with condition that cell to traverse to must have height greater or equal to current cell


## Code

```python
class Solution:

    def floodFill(self, heights, row, col, ocean):
        # assumes already reachable from ocean

        m = len(heights)
        n = len(heights[0])

        if ocean[row][col] is True:
            return ocean[row][col]

        ocean[row][col] = True

        children = []

        if row > 0 and heights[row-1][col] >= heights[row][col]:
            children.append({'row': row-1, 'col': col})
        if row < m-1 and heights[row+1][col] >= heights[row][col]:
            children.append({'row': row+1, 'col': col})
        if col > 0 and heights[row][col-1] >= heights[row][col]:
            children.append({'row': row, 'col': col-1})
        if col < n-1 and heights[row][col+1] >= heights[row][col]:
            children.append({'row': row, 'col': col + 1})

        for child in children:
            self.floodFill(heights, child['row'], child['col'], ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        pacific = [[None] * n for i in range(m)]
        atlantic = [[None] * n for i in range(m)]

        for i in range(m):
            self.floodFill(heights, i, 0, pacific)

        for i in range(n):
            self.floodFill(heights, 0, i, pacific)

        for i in range(m):
            self.floodFill(heights, i, n-1, atlantic)

        for i in range(n):
            self.floodFill(heights, m-1, i, atlantic)

        result = []

        for row in range(m):
            for col in range(n):
                if pacific[row][col] is True and atlantic[row][col] is True:
                    result.append([row, col])

        return result

```
