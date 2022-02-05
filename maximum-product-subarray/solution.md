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


