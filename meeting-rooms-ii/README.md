# Meeting Rooms II

## Link

https://leetcode.com/problems/meeting-rooms-ii/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

## Solution Main Idea

Sort intervals by starttime. Have a minheap on endtime, where it represents the list of rooms. Top of heap is therefore most likely to be free. Add to heap a new room if no room free
