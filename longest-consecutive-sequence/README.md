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
