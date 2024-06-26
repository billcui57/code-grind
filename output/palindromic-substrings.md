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


## Code

```python
class Solution:
    # palindrome finder for palindromes rooted at s[left:right+1]
    def helper(self, s, left, right):

        count = 1

        while left - 1 >= 0 and right + 1 < len(s):
            if s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                count += 1
            else:
                return count

        return count

    def countSubstrings(self, s: str) -> str:

        counter = 0

        for i in range(len(s)):

            # if applicable, also include palindromes rooted at s[i:i+1]
            if i + 1 < len(s) and s[i] == s[i + 1]:
                counter += self.helper(s, i, i + 1)

            counter += self.helper(s, i, i)

        return counter

```
