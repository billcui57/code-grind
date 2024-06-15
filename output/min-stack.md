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


## Code

```python
import heapq
class MinStack:

    def __init__(self):
        self.container = dict()
        self.heap = []
        self.stack = []
        

    def push(self, val: int) -> None:
        if val not in self.container:
            self.container[val] = 1
        else:
            self.container[val] += 1
        heapq.heappush(self.heap, val)
        self.stack.append(val)
        

    def pop(self) -> None:
        top = None
        while(True):
            top = self.stack.pop()
            if top in self.container and self.container[top] > 0:
                break
        if top is not None:
            self.container[top] -= 1
        

    def top(self) -> int:
        top = None
        while(True):
            top = self.stack[-1]
            if top in self.container and self.container[top] > 0:
                break
            self.stack.pop()
        return top
        

    def getMin(self) -> int:
        minEl = None
        while(True):
            minEl = self.heap[0]
            if minEl in self.container and self.container[minEl] > 0:
                break
            heapq.heappop(self.heap)
        return minEl
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```
