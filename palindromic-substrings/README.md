# Palindromic Substrings

## Link

https://leetcode.com/problems/palindromic-substrings/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

## Solution Main Idea

For each index $i$, obtain all palindromes rooted at $s[i]$ and $s[i:i+1]$ (is applicable) and accumulate.
