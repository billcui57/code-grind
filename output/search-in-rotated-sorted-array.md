# Search in Rotated Sorted Array

## Link

https://leetcode.com/problems/search-in-rotated-sorted-array/description/

## Where

Leetcode

## Difficulty

Medium

## Description

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

## Solution Main Idea

Binary search for min
Use min index as offset to map


## Code

```python
class Solution:

    def get_min(self,nums):
        lo = 0
        hi = len(nums)-1

        while lo < hi:
            if nums[lo] < nums[hi]: #array has no shift
                return lo
            
            middle = (lo + hi)//2

            if nums[middle] > nums[middle+1]: #pivot is at middle +1
                return middle+1
            

            if nums[lo] < nums[middle]: #pivot is to the right
                lo = middle+1
                continue
            if nums[lo] > nums[middle]: #pivot is to the left
                hi = middle
                continue
        return hi
    


            
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.get_min(nums)
        lo = 0
        hi = len(nums)-1
        def mapper(index):
            return (min_index+index)%len(nums)
        while lo <= hi:
            middle = (lo + hi)//2
            if target < nums[mapper(middle)]:
                hi = middle-1
                continue
            if target > nums[mapper(middle)]:
                lo = middle+1
                continue
            return mapper(middle)
        return -1
                



```
