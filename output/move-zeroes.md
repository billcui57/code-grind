# Move Zeroes

## Link

https://leetcode.com/problems/move-zeroes/description/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## Solution Main Idea

Iterate from left to right, keep track of index of first 0 in list. When we see a non-zero, swap with first 0.


## Code

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        
```
