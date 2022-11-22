# Longest Increasing Subsequence

## Link

https://leetcode.com/problems/longest-increasing-subsequence/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

## Solution Main Idea

Let $A[i]$ denote the LIS that ends at index $i$.

$$A[i] = max(A[j]+1: j<i, N[j]<N[i])$$

max over all $A[i]$'s

Base case: all $A[i]$'s = 1
