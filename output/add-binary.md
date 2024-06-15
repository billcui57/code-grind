# Add Binary

## Link

https://leetcode.com/problems/add-binary/

## Where

Leetcode

## Difficulty

Easy

## Description

Given two binary strings a and b, return their sum as a binary string.

## Solution Main Idea

Implement binary adding or use python built-in


## Code

```python
# No built-in:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aRev = list(reversed(a))
        bRev = list(reversed(b))

        aPtr = 0
        bPtr = 0

        carry = "0"
        result = []

        while aPtr < len(aRev) and bPtr < len(bRev):
            if aRev[aPtr] == "1" and bRev[bPtr] == "1":
                if carry == "1":
                    result.append("1")
                else:
                    carry = "1"
                    result.append("0")
            elif aRev[aPtr] == "0" and bRev[bPtr] == "0":
                if carry == "1":
                    result.append("1")
                    carry = "0"
                else:
                    result.append("0")
            else:
                if carry == "1":
                    result.append("0")
                else:
                    result.append("1")
            aPtr += 1
            bPtr += 1
        while aPtr < len(aRev):
            if aRev[aPtr] == "1":
                if carry == "1":
                    result.append("0")
                else:
                    result.append("1")
            else:
                if carry == "1":
                    result.append("1")
                    carry = "0"
                else:
                    result.append("0")
            aPtr += 1
        while bPtr < len(bRev):
            if bRev[bPtr] == "1":
                if carry == "1":
                    result.append("0")
                else:
                    result.append("1")
            else:
                if carry == "1":
                    result.append("1")
                    carry = "0"
                else:
                    result.append("0")
            bPtr += 1
        if carry == "1":
            result.append("1")
        return "".join(list(reversed(result)))


# Built-in:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

```
