# Linked List Cycle

## Link

https://leetcode.com/problems/linked-list-cycle/

## Where

Leetcode

## Difficulty

Easy

## Description

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

## Solution Main Idea

Use two pointers. One fast and one slow. Fast pointer moves forward twice for every time slow pointer moves forward once. If they land on the same node then there is a cycle


## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        slow_move = False

        while fast and slow:
            fast = fast.next
            if slow_move:
                slow = slow.next

            slow_move = not slow_move

            if fast is slow:
                return True

        return False

```
