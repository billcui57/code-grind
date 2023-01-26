# Min Stack

## Link

https://leetcode.com/problems/min-stack/

## Where

Leetcode

## Difficulty

Medium

## Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

## Solution Main Idea

Have a container dict to keep track of which elements are actually in the data structure.
When we pop min or just pop, pop until all shadow elements are gone.
