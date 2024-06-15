# Letter Combinations of a Phone Number

## Link
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

## Where
Leetcode

## Difficulty
Medium

## Description
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

## Solution Main Idea
Create adj based on mapping
Perform DFS

## Code

```python
class Solution:

    def dfs(self, digits, build, map,result):
        if len(digits) == 0:
            if build != "":
                result.append(build)
            return
        front = digits.pop()
        letters = map[front]
        for letter in letters:
            self.helper(digits, build+letter, map, result)
        digits.append(front)


    def letterCombinations(self, digits: str) -> List[str]:
        digits = list(reversed(digits))

        map = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        build = ""
        result = []
        self.dfs(digits, build, map, result)
        return result



```
