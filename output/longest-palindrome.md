# Longest Palindrome

## Link

https://leetcode.com/problems/longest-palindrome/

## Where

Leetcode

## Difficulty

Easy

## Description

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

## Solution Main Idea

Use counter and add multiples of 2. If there are any word freqs left then can add 1 as the middle


## Code

```python
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        wordFreq = Counter(s)
        length = 0
        usedMiddle = False

        for letter, freq in wordFreq.items():
            canUse = (freq // 2) * 2
            length += canUse
            remaining = max(0, freq - canUse)
            if remaining > 0 and usedMiddle is False:
                length += 1
                usedMiddle = True

        return length

```
