# Word Break II

## Link

https://leetcode.com/problems/word-break-ii/description/

## Where

Leetcode

## Difficulty

Hard

## Description

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Solution Main Idea

Split the string at all indexes. Then basically there is always two parts - the first part (word) and rest of the string. If word is in the wordDict, take the second part, and do the same thing until there is no string left. At that point, simply join the path with space and append to the output.

Convert wordDict to hashset for O(1) lookup time.


## Code

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def recur(s, path):
            if not s:
                out.append(' '.join(path))
                return
            for i in range(1,len(s)+1):
                w,new_s = s[:i], s[i:]
                if w in wordDict:
                    recur(new_s, path + [w])
        wordDict, out = set(wordDict), []
        recur(s,[])
        return out
```
