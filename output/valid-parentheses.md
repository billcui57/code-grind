# Valid Parentheses

## Link

https://leetcode.com/problems/valid-parentheses/

## Where

Leetcode

## Difficulty

Easy

## Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

## Solution Main Idea

Use a stack that represents opening brackets. A closing bracket must match the opening bracket at top of stack to be valid. If they match then pop from stack. The stack grows when we see an opening bracket. Whole string is valid only if stack is empty in the end.


## Code

```python
class Solution:

    brackMap = {"(": ")", "[": "]", "{": "}"}

    def isValid(self, s: str) -> bool:

        openStack = []

        for i in range(len(s)):
            if s[i] in self.brackMap:
                openStack.append(s[i])
            else:
                if len(openStack) > 0 and self.brackMap[openStack[-1]] == s[i]:
                    openStack.pop()
                else:
                    return False
        return len(openStack) == 0

```
