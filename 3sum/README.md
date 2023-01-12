# 3Sum

## Link

https://leetcode.com/problems/3sum/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

## Solution Main Idea

Use twosum to solve threesum. For each index $i$ in $num$, let twoSum find the two indices $j$, $k$ in $num[i+1:]$ such that $num[j] + num[k] = -num[i]$. Sort the array first so that all result tuples follow invariant of solution: a[i] <= a[j] <= a[k].
Store result in tuple so we can hash it. The invariant allows for hashing to remove duplicates
