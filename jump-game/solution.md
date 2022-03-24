# Jump Game

## Link

https://leetcode.com/problems/jump-game/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

## Solution Main Idea

Use DP. Let $A[i]$ represent the furthest one could reach by jumping through a particular subsequence in $nums[0:i]$ that ends at $i$.
If $A[i-1] >= i$, meaning we can jump to $i$, then $A[i] = max(A[i-1], i + nums[i])$. (If we jump from $i$, then the furthest we can go from $i$ is $i + nums[i]$, if we don't jump from $i$, then in order to proceed we must jump from somewhere before $i$, and furthest we could jump from before $i$ is $A[i-1]$.)
