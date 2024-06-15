# Maximum Value after Insertion

## Link
https://leetcode.com/problems/maximum-value-after-insertion/description/

## Where
Leetcode

## Difficulty
Medium

## Description
You are given a very large integer n, represented as a string,​​​​​​ and an integer digit x. The digits in n and the digit x are in the inclusive range [1, 9], and n may represent a negative number.

You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n​​​​​​. You cannot insert x to the left of the negative sign.

For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
Return a string representing the maximum value of n​​​​​​ after the insertion.

## Solution Main Idea
Digits further to the left have more impact on the value of the number. We wish to add the digit at the location with most impact
while not overriding digits that would have more impact than the digit we are inserting. Therefore, we greedily go from left to right, finding a location where the value of digits is less than the digit we are adding. Opposite is true for negative

## Code

```python
class Solution:
    def maxValue(self, n: str, x: int) -> str:
        result = None
        isNegative = False
        i = 0
        while i < len(n):
            if n[i] == "-":
                isNegative = True
                i+=1
                continue
            if isNegative:
                if x >= int(n[i]):
                    i+=1
                    continue
            else:
                if x <= int(n[i]):
                    i+=1
                    continue
            break
        result = n[:i] + str(x) + n[i:]
        return result
```
