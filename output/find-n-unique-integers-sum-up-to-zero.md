# Find N Unique Integers Sum up to Zero

## Link
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

## Where
Leetcode

## Difficulty
Easy

## Description
Given an integer n, return any array containing n unique integers such that they add up to 0.

## Solution Main Idea
Palindrome of negative and positive


## Code

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result = [0]
            n = n-1
        
        for i in range(1,(n//2)+1):
            result = [-1 * i] + result + [i]
        
        return result
        

```
