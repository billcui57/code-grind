# Merge Intervals

## Link

https://leetcode.com/problems/merge-intervals/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Solution Main Idea

Sort by start, have result list, check if last element in result list overlaps with cur interval, merge and append.
