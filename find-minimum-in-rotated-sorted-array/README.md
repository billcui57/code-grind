# Find Minimum in Rotated Sorted Array

## Link
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

## Where
Leetcode

## Difficulty
Medium

## Description
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

## Solution Main Idea

Divide and conquer using binary search. An inflection point is defined to be between $i$ and $i+1$ where $A[i-1] < A[i] > A[i+1]$. $A[i]$ would be the biggest element in nums, and $A[i+1]$ would be the smallest. 

All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.

4 5 6 7 2 3

1. Find the mid element of the array.

2. If mid element > first element of array this means that we need to look for the inflection point on the right of mid.

3. If mid element < first element of array this that we need to look for the inflection point on the left of mid.
