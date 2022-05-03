# Find Median from Data Stream

## Link

https://leetcode.com/problems/find-median-from-data-stream/

## Where

Leetcode

## Difficulty

Hard

## Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

## Solution Main Idea

Have two heaps, one max heap for holding values less than and including median, one minheap for holding values greater than medium. Rebalance to maintain that invariant
