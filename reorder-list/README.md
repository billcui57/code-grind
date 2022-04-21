# Reorder List

## Link

https://leetcode.com/problems/reorder-list/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Solution Main Idea

Three steps. Find middle node, reverse list at middle node, reorder by alternate setting heads
