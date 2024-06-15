# Maximum Number of Balloons

## Link
https://leetcode.com/problems/maximum-number-of-balloons/description/

## Where
Leetcode

## Difficulty
Easy

## Description
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

## Solution Main Idea
Create a counter of letters. Keep trying to more freq of "balloon" until you cant.

## Code

```python
from collections import Counter
class Solution:

    def remove_balloon(self, counter):

        for c in "balloon":
            if c not in counter:
                return False
            if counter[c] == 0:
                return False
            counter[c] -=1
        return True


    def maxNumberOfBalloons(self, text: str) -> int:

        text_counter = Counter(list(text))

        result = 0
        while self.remove_balloon(text_counter):
            result+=1
        return result

        
```
