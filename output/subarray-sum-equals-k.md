# Subarray Sum Equals K

## Link

https://leetcode.com/problems/subarray-sum-equals-k/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

## Solution Main Idea

The idea behind this approach is as follows: If the cumulative sum up to two indices is the same, the sum of the elements lying in between those indices is zero. Extending the same thought further, if the cumulative sum up to two indices, say sum[i] and sum[j] is at a difference of k, the sum of elements lying between indices i and j is k. Store this in hashmap alongside num of occurrences. Key is cum sum. Value is num occurrences.
x

## Code

```python

```
