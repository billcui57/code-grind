# Decode String

## Link

https://leetcode.com/problems/decode-string/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

## Solution Main Idea

Use a stack. Invariant: by the time you reach a closing bracket, the top of the stack contains only terminal strings. So just multiply by freq and add to next level in stack.


## Code

```python
class Solution:
    def decodeString(self, s: str) -> str:
        s = list(s)

        stack = []

        i = 0
        number=""

        result = ""
        while i < len(s):
            if s[i].isnumeric():
                number += s[i]
            elif s[i] == "[":
                stack.append([int(number),""])
                number =""
            elif s[i] == "]":
                freq,part = stack.pop()
                if len(stack) > 0:
                    stack[-1][1] += part * freq
                else:
                    result += part * freq
            else:
                if len(stack) > 0:
                    stack[-1][1] += s[i]
                else:
                    result += s[i]
            i += 1
        return result
        





























```
