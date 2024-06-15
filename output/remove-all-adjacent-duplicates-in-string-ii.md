# Remove All Adjacent Duplicates in String II

## Link

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

## Solution Main Idea

Stack, each element holds char and its frequency. If frequency == k then pop off stack. Afterwards just return char \* frequency


## Code

```python
class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:

        stack = []

        for char in s:
            if len(stack) > 0 and char == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([char,1])
                
            if len(stack) > 0 and stack[-1][1] == k:
                stack.pop()
        return "".join([x[0]*x[1] for x in stack])
```
