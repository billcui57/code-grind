# 3Sum

## Link

https://leetcode.com/problems/3sum/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Solution Main Idea

Use twosum to solve threesum. For each index $i$ in $num$, let twoSum find the two indices $j$, $k$ in $num[i+1:]$ such that $num[j] + num[k] = -num[i]$. Sort the array first so that all result tuples follow invariant of solution: a[i] <= a[j] <= a[k].
Store result in tuple so we can hash it. The invariant allows for hashing to remove duplicates


## Code

```python
class Solution:
    def twoSum(self, start, nums, target):
        seen = set()
        result = []
        
        for i in range(start, len(nums)):
            if target - nums[i] in seen:
                result.append((nums[i], target-nums[i]))
            seen.add(nums[i])
        return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        #invariant of solution: a[i] <= a[j] <= a[k]

        result = set()

        for i in range(len(nums)):
            twoSumResults = self.twoSum(i+1, nums, -1 * nums[i])
            for a,b in twoSumResults:
                result.add((a,b,nums[i]))
        
        return [[a,b,c] for a,b,c in list(result)]
                






```
