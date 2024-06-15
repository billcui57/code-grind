# Spiral Matrix III

## Link
https://leetcode.com/problems/spiral-matrix-iii/description/

## Where
Leetcode

## Difficulty
Medium

## Description
You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.

## Solution Main Idea
We increase the stepVal every time after we have moved two directions. Set upper bound to be 2 * max(rows,cols) increases


## Code

```python
class Solution:

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        # step increases by 1 after every 2 direction moves

        rLoc = rStart
        cLoc= cStart
        stepVal = 1


        def getDelta():
            i = 0
            while True:
                if i== 0:
                    yield (0, 1)
                elif i==1:
                    yield (1 ,0)
                elif i==2:
                    yield (0, -1)
                else:
                    yield (-1, 0)
                i = (i+1)%4

        getDeltaGen = getDelta()
        result = []
        result.append([rLoc, cLoc])

        for i in range(2 * max(rows,cols)):
            for dirMove in range(2):
                rDelta, cDelta = next(getDeltaGen)
                for step in range(stepVal):
                    rLoc += rDelta
                    cLoc += cDelta
                    if rLoc < rows and cLoc < cols and rLoc > -1 and cLoc > -1:
                        result.append([rLoc, cLoc])
            stepVal +=1
        return result

```
