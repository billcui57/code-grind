# Longest Palindromic Substring

## Link

https://leetcode.com/problems/longest-palindromic-substring/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a string s, return the longest palindromic substring in s.

## Solution Main Idea

At each index $i$ obtain the local longest palindrome rooted at $i$. Be mindful of palindromes rooted at $i$ and $i+1$ as well. Then achieve a global longest palindrome
