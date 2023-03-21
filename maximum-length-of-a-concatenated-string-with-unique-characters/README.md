# Maximum Length of a Concatenated String with Unique Characters

## Link
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

## Where
Leetcode

## Difficulty
Medium

## Description
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

## Solution Main Idea
O(2^n) solution since we explore all possible subsequences of arr of len N

Solution 1:
Recursion
For each index, explore adding each index after it. Check if there are duplicates

Solution 2:
Build on top of solution 1 to use bitmaps to store result. Greatly reduces space complexity O(N) space