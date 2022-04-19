# Merge k Sorted Lists

## Link

https://leetcode.com/problems/merge-k-sorted-lists/

## Where

Leetcode

## Difficulty

Hard

## Description

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Solution Main Idea

Use a min heap PQ that holds the heads of all linked lists. Pop the head from the top of the PQ and append it to the back of the new linked list. Add the next of head back into PQ. Continue until PQ is empty
