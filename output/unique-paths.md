# Unique Paths

## Link

https://leetcode.com/problems/unique-paths/

## Where

Leetcode

## Difficulty

Medium

## Description

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 \* 109.

## Solution Main Idea

Use DP. Let $A[i][j]$ represent the number of ways to reach row $i$ col $j$. $A[i][j] = A[i-1][j] + A[i][j-1]$.
Return $A[n-1][m-1]$


## Code

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        A = [[0] * m] * n

        A[0][0] = 1

        for i in range(1, n):
            A[i][0] = A[i-1][0]

        for j in range(1, m):
            A[0][j] = A[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                A[i][j] = A[i-1][j] + A[i][j-1]

        return A[n-1][m-1]

```
