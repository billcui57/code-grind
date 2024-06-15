# Maximum Product Subarray

## Link
https://leetcode.com/problems/maximum-product-subarray/

## Where
Leetcode

## Difficulty
Medium

## Description
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

## Solution Main Idea

Similar to maximum-subarray problem. DP.  Let local_max[i] denote the largest product among all subarrays of $nums$ that end at index i.
local_max[i] denote the smallest product among all subarrays of $nums$ that end at index i. If $nums[i]$ is negative, then what was local max in the previous
i might very well be the smallest in this i. What was local min in the previous i might be the biggest in this i. We also have to consider $num[i]$ on its own as well




## Code

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        local_min = [1] * len(nums)
        
        local_max = [1] * len(nums)
    
        
        local_min[0] = nums[0]
        local_max[0] = nums[0]
        
        total_max = -inf
        
        for i in range(1, len(nums)):
            
            if nums[i] >=0 :

                local_max[i] = max( local_max[i-1] * nums[i] , nums[i]) 

                local_min[i] = min( local_min[i-1] * nums[i] , nums[i])

            else:

                local_max[i] = max (local_min[i-1] * nums[i], nums[i])

                local_min[i] = min (local_max[i-1] * nums[i], nums[i])
            
            
            if local_max[i] > total_max:
                total_max = local_max[i]
        
        return max(local_max[0], total_max)
        
        
        
        
        
        
        
        
        
               
        
```
