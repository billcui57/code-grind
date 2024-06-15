# Valid Palindrome

## Link

https://leetcode.com/problems/valid-palindrome/

## Where

Leetcode

## Difficulty

Easy

## Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

## Solution Main Idea

Left and right pointers


## Code

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True

```
