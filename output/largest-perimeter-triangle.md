# Largest Perimeter Triangle

## Link
https://leetcode.com/problems/largest-perimeter-triangle/description/

## Where
Leetcode

## Difficulty
Easy

## Description
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

## Solution Main Idea
Sort the list ascending. At any index, the best bet that it will be a valid triangle are the two indices before it (they're the next biggest). It also happens that if they are valid, then those two will be the biggest triangle for that root index.

## Code

```python
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest = 0

        nums = list(sorted(nums))

        for i in range(2, len(nums)):
            if nums[i-1] + nums[i-2] > nums[i]:
                largest = max(nums[i-1] + nums[i-2] + nums[i], largest)
        return largest

```
