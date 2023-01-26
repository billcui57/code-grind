# Remove All Adjacent Duplicates in String II

## Link

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

## Solution Main Idea

Stack, each element holds char and its frequency. If frequency == k then pop off stack. Afterwards just return char \* frequency
