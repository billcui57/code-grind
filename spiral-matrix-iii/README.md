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
