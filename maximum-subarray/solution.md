# maximum-subarray

## Link

https://leetcode.com/problems/maximum-subarray/submissions/

## Where

Leetcode

## Difficulty

Easy

## Description

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

## Solution Main Idea

Divide and conquer. Get the maximum sum of left subarray (start...mid), right subarray (mid+1...end), and the subarray that passes through the midpoint.
To find the max of subarray that passes through the midpoint it is found by finding max subarray of start...mid rooted at mid + finding max subarray of mid+1...end rooted at mid+1.



