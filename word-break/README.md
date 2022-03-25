# Word Break

## Link

https://leetcode.com/problems/word-break/submissions/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Solution Main Idea

Use DP. let $A[i]$ represent whether or not we can express suffix $s[i:]$ as a combination of wordDict. For each word $matchingPrefix$ that matches the prefix of the suffix $s[i:]$, $A[i] = A[i+len(matchingPrefix)] or A[i]$ (We use it or dont use it). Return $A[0]$

Or

Use BFS. Let $s$ be a vertex such that $vertices[s]$ is a string. Get all possible words in wordDict that is a prefix of $vertices[s]$ and set
the suffix of $vertices[s]$ excluding them as adjacent to $vertices[s]$. Let $vertices[""]$ be the vertex we wish to visit. Run BFS from $vertices[s]$
and return true if we visit $vertices[""]$. Else false.
