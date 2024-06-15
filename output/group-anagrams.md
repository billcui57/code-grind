# Group Anagrams

## Link

https://leetcode.com/problems/group-anagrams/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Solution Main Idea

Sort the strings and add to dictionary, then convert dictionary into list of lists


## Code

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        
        for string in strs:
            sortedString = "".join(sorted(string))
            
            if sortedString not in groups:
                groups[sortedString] = [string]
            else:
                groups[sortedString].append(string)
        
        result = []
        
        for sortedString in groups:
            result.append(groups[sortedString])
        
        return result
```
