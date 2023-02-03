# Move Zeroes

## Link

https://leetcode.com/problems/move-zeroes/description/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

## Solution Main Idea

Iterate from left to right, keep track of index of first 0 in list. When we see a non-zero, swap with first 0.
