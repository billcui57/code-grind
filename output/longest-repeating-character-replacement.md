# Longest Repeating Character Replacement

## Link

https://leetcode.com/problems/longest-repeating-character-replacement/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Solution Main Idea

Sliding window. Keep track of freq of all letters inside head and tail inclusive. The number of changes needed to make s[head, tail inc] valid is $head - tail + 1 - freq[mostFreqLetter]$. Valid iff $\le k$.

Inc tail if not valid and remove from freq dict. We can determine if $s[head, tail inc]$ is valid without needing to know if the previous $s[head, tail inc]$ was valid or not, so doesn't matter if its valid or not, always increment head.


## Code

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        freqDict = {}
        head = 0
        tail = 0
        s = list(s)
        longestLength = 0
        mostFreqLetter = None

        while head < len(s):
            if s[head] in freqDict:
                freqDict[s[head]] += 1
            else:
                freqDict[s[head]] = 1

            mostFreqLetter = (
                s[head]
                if not mostFreqLetter or freqDict[s[head]] > freqDict[mostFreqLetter]
                else mostFreqLetter
            )

            highestFreq = freqDict[mostFreqLetter]

            neededChanges = (head - tail + 1) - highestFreq

            if neededChanges <= k:
                longestLength = max(longestLength, head - tail + 1)
            else:
                freqDict[s[tail]] -= 1
                tail += 1
            head += 1
        return longestLength

```
