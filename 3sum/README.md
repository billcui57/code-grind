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

Use twosum to solve threesum. For each index $i$ in $num$, let twoSum find the two indices $j$, $k$ in $num[i+1:]$ such that $num[j] + num[k] = -num[i]$. Store these
triplets in a seen table. A seen table is a table of tables where $[a,b,c]$ is in seen table if $a$ in $seen$ and $b$ in $seen[a]$ and $c$ in $seen[a][b]$. To add to seen table add element wise from $a$ first then to $c$
