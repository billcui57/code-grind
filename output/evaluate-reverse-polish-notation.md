# Evaluate Reverse Polish Notation

## Link

https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '\*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.

## Solution Main Idea

Write a postfix evaluator. Pop from back. When all left is popped away, right is what is left.
Or you can write an AST and traverse it


## Code

```python
class Solution:
    
    operators = set(["+","-","*","/"])

    def operate(self, left, right, operator):
        if operator == "+":
            return left + right
        if operator == "-":
            return left - right
        if operator == "*":
            return left *right
        if operator == "/":
            return int(left/right)

    def eval(self, tokens):
        el = tokens.pop()
        if el in self.operators:
            right = self.eval(tokens)
            left = self.eval(tokens)
            return self.operate(left,right, el)
        return int(el)

    def evalRPN(self, tokens: List[str]) -> int:
        result = self.eval(tokens)
        return result
```
