# Longest Consecutive Sequence

## Link

https://leetcode.com/problems/longest-consecutive-sequence/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

## Solution Main Idea

Use DP. Let maxLength memo the best solution we have so far. Convert $nums$ to a set to ignore duplicates as they do not matter. Find the longest streak by first finding the smallest in a streak and iteratively looking if its +1 exists. Each streak is mutually exclusive so $O(n)$


## Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxLength = 0

        numSet = set(nums)

        # duplicates dont matter so we ignore it to be faster
        for x in numSet:
            length = 1
            if x-1 not in numSet:
                oneBigger = x + 1
                while oneBigger in numSet:
                    length += 1
                    oneBigger += 1

            maxLength = max(length, maxLength)

        return maxLength

```
