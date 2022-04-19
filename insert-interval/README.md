# Insert Interval

## Link

https://leetcode.com/problems/insert-interval/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

## Solution Main Idea

Cases:
The interval appears entirely before intervals
The interval appears entirely after intervals
The interval appears inside intervals but not intersecting
The interval appears inside intervals but is intersecting.

Deal with fourth case by finding the start and end values of the merged interval using min and max
