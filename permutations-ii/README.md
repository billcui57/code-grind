# Permutations II

## Link

https://leetcode.com/problems/permutations-ii/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

## Solution Main Idea

Use backtracking. Keep track of each num's frequency (amount of each num that is available). For each num that is available and has not yet been chosen already in this stage of recursion, choose it (prune others by not recursing into it - backtracking). Recurse and treat result as list of prefix of the array. Append num to the end of the array. Add array to the result array and return that.

(We do this to use .append which takes O(1))

{1,1,2,3}, choose 1: {1,2,3}[1], choose 2: {1,3}[2,1],

choose 3: {1}[3,2,1], choose 1: {}[1,3,2,1]

, choose 1: {3}[1,2,1], choose 3: {}[3,1,2,1]

, choose 1: {2,3}[1,1], choose 2: {3}[2,1,1], choose 3: {}[3,2,1,1]

, choose 3: {2}[3,1,1], choose 2: {}[2,3,1,1]

...

, #DONT CHOOSE 1 AGAIN

, choose 2: {1,1,3}[2]...

....
