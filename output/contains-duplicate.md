# Contains Duplicate

## Link

https://leetcode.com/problems/contains-duplicate/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

## Solution Main Idea

Keep dictionary of num frequency, find values in dictionary with frequency $\geq$ 2


## Code

```python
def containsDuplicate(self, nums: List[int]) -> bool:
    seenNums = {}

    for num in nums:
        if num not in seenNums:
            seenNums[num] = 1
        else:
            seenNums[num] += 1

    for num in seenNums.values():
        if num >= 2:
            return True

    return False

```
