# Longest Repeating Character Replacement

## Link

https://leetcode.com/problems/longest-repeating-character-replacement/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Solution Main Idea

Sliding window. Keep track of freq of all letters inside head and tail inclusive. The number of changes needed to make s[head, tail inc] valid is $head - tail + 1 - freq[mostFreqLetter]$. Valid iff $\le k$.

Inc tail if not valid and remove from freq dict. We can determine if $s[head, tail inc]$ is valid without needing to know if the previous $s[head, tail inc]$ was valid or not, so doesn't matter if its valid or not, always increment head.
