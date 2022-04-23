# Longest Substring Without Repeating Characters

## Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a string s, find the length of the longest substring without repeating characters.

## Solution Main Idea

Sliding Window, head and tail. If we haven't seen $s[head]$ before then $s[tail, head inc]$ is the longest valid substring that ends at $head$. We then inc head. If we have seen $s[head]$ before then we inc $tail$ and remove from set until we reach scenario 1, in which $s[tail, head inc]$ is the longest valid substring that ends at $head$.

Think about how this is a subset of DP. Use a valid $s[tail, head inc]$ to efficiently find the next $s[tail, head inc]$ after inc head by 1.

Unlike longest-repeating-character-replacement, we cannot inc head if its invalid, because we cannot test if $s[tail, head]$ is valid after we have moved head. (Moving head when its invalid is dangerous as we can get false positives for validity from just testing $s[head]$, we don't have enough info from just $s[head]$ alone without knowing if the previous $s[tail,head]$ was valid or not)
