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


## Code

```python
class Solution:

    def prefixHasMatch(self, s: str, wordDict):

        matchingWords = []

        for word in wordDict:
            if s.find(word) == 0:
                matchingWords.append(word)

        return matchingWords

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        A = [False] * (len(s) + 1)

        A[len(s)] = True

        for i in reversed(range(len(s) + 1)):
            matchingPrefixes = self.prefixHasMatch(s[i:], wordDict)
            for matchingPrefix in matchingPrefixes:
                A[i] = A[i+len(matchingPrefix)] or A[i]

        return A[0]


class Solution:

    def prefixHasMatch(self, s: str, wordDict):

        matchingWords = []

        for word in wordDict:
            if s.find(word) == 0:
                matchingWords.append(word)

        return matchingWords

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        queue = []
        visited = set()

        queue.append(s)

        while len(queue) > 0:
            node = queue.pop()

            visited.add(node)

            matchingPrefixes = self.prefixHasMatch(node, wordDict)

            for matchedPrefix in matchingPrefixes:
                suffix = node[len(matchedPrefix):]

                if suffix == "":
                    return True

                if suffix not in visited:
                    queue.append(suffix)

        return False

```
