# Longest Substring Without Repeating Characters

## Link

https://leetcode.com/problems/longest-substring-without-repeating-characters/

## Where

Leetcode

## Difficulty

Medium

## Description

Given a string s, find the length of the longest substring without repeating characters.

## Solution Main Idea

Sliding Window, head and tail. If we haven't seen $s[head]$ before then $s[tail, head inc]$ is the longest valid substring that ends at $head$. We then inc head. If we have seen $s[head]$ before then we inc $tail$ and remove from set until we reach scenario 1, in which $s[tail, head inc]$ is the longest valid substring that ends at $head$.

Think about how this is a subset of DP. Use a valid $s[tail, head inc]$ to efficiently find the next $s[tail, head inc]$ after inc head by 1.

Unlike longest-repeating-character-replacement, we cannot inc head if its invalid, because we cannot test if $s[tail, head]$ is valid after we have moved head. (Moving head when its invalid is dangerous as we can get false positives for validity from just testing $s[head]$, we don't have enough info from just $s[head]$ alone without knowing if the previous $s[tail,head]$ was valid or not)


## Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        head = 0
        tail = 0
        seen = set()

        maxLength = 0

        while head < len(s):
            if s[head] not in seen:
                seen.add(s[head])
                maxLength = max(head - tail + 1, maxLength)
                head += 1
            else:
                # keep removing until we remove the repeating char
                seen.remove(s[tail])
                tail += 1

        return maxLength


# or (better)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = dict()

        lo = 0
        hi = 0

        s= list(s)

        best = 0
        while hi < len(s):
            # maintain invariant that s[lo:hi] contains no repeating characters 
            if s[hi] in seen:
                seenIndex = seen[s[hi]]
                for i in range(lo, seenIndex+1):
                    seen.pop(s[i])
                lo = seenIndex+1
            seen[s[hi]] = hi

            best = max(hi-lo+1, best)

            hi+=1
        return best



```
