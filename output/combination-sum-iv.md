# Combination Sum 4

## Link

https://leetcode.com/problems/combination-sum-iv/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

## Solution Main Idea

Use DP. Let A[i] be the number of permutations to reach $i$. For each $i$, go through each num in nums, such that $A[i] = A[i - num] + A[i]$ (We take it or not)


## Code

```python
class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:

        A = [0] * (target + 1)

        A[0] = 1

        for amount in range(target+1):
            for num in nums:
                if amount - num >= 0:
                    A[amount] = A[amount - num] + A[amount]

        return A[target]

```
