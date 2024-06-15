# Climbing Stairs

## Link

https://leetcode.com/problems/climbing-stairs/

## Where

Leetcode

## Difficulty

Easy

## Description

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Solution Main Idea

Use DP. Let $totalSteps[i]$ denote the num of distinct ways to reach the top when you're at step $i$. step 0 indicates that you're not on the stairs yet. step $n$ indicates you're at the top.

Fill in $totalSteps$ from $n$ to $0$. $totalSteps[i] = totalSteps[i+1] + totalSteps[i+2]$


## Code

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        totalSteps = [0] * (n+1)

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        totalSteps[len(totalSteps)-1] = 0
        totalSteps[len(totalSteps)-2] = 1
        totalSteps[len(totalSteps)-3] = 2

        for i in reversed(range(len(totalSteps)-3)):
            totalSteps[i] = totalSteps[i+1] + totalSteps[i+2]

        return totalSteps[0]

```
