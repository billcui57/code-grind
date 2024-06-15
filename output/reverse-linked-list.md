# Reverse Linked List

## Link

https://leetcode.com/problems/reverse-linked-list/

## Where

Leetcode

## Difficulty

Easy

## Description

Given the head of a singly linked list, reverse the list, and return the reversed list.

## Solution Main Idea

Keep track of oldhead and newhead.


## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        previous, current, next = None, head, None
        while current is not None:
            next = current.next  # temporarily store the next node
            current.next = previous  # reverse the current node
            previous = current  # point previous to the current node
            current = next  # move on
        return previous

```
