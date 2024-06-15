# Decode Ways

## Link

https://leetcode.com/problems/decode-ways/

## Where

Leetcode

## Difficulty

Medium

## Description

A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.

## Solution Main Idea

Use DP. Similar to work-break. Let $A[i]$ represent the number of ways to decode in suffix $s[i:]$. For each $s[i:]$, find all mappings that
matches the prefix of $s[i:]$, and add up the number of ways to decode all suffixes that have the prefix removed.

$A[i] += A[i + len(match)]$


## Code

```python
class Solution:

    def prefixHasMatch(self, s, mapping):

        matches = []

        for i in range(len(s)):
            if s[0:i+1] in mapping:
                matches.append(s[0:i+1])

        return matches

    def numDecodings(self, s: str) -> int:

        mapping = set([str(i) for i in range(1, 27)])

        A = [0] * (len(s) + 1)

        A[len(s)] = 1

        for i in reversed(range(len(s))):
            matches = self.prefixHasMatch(s[i:], mapping)
            A[i] = 0
            for match in matches:
                A[i] += A[i + len(match)]

        return A[0]

```
