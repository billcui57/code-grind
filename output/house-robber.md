# House Robber

## Link

https://leetcode.com/problems/house-robber/

## Where

Leetcode

## Difficulty

Medium

## Description

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Solution Main Idea

Use DP. Let $A[i]$ be the maximum amount of money you can steal from houses in $nums[0:i]$ (subarray of $nums$ ending at $i$).

$A[i] = max(nums[i] + A[i-2] \text{(include if i - 2 >=0)}, A[i - 1])$ (Steal from $i$ or not). Return $A[len(nums)-1]$


## Code

```python
class Solution:
    def rob(self, nums: List[int]) -> int:

        A = [-inf] * len(nums)

        A[0] = nums[0]

        for houseIndex in range(1, len(nums)):
            if houseIndex - 2 >= 0:
                A[houseIndex] = max(nums[houseIndex] +
                                    A[houseIndex-2], A[houseIndex - 1])
            else:
                A[houseIndex] = max(nums[houseIndex], A[houseIndex - 1])

        return A[len(nums) - 1]

```
