# Middle of the Linked List

## Link
https://leetcode.com/problems/middle-of-the-linked-list/

## Where
Leetcode

## Difficulty
Easy

## Description
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

## Solution Main Idea
Traverse once to get length, traverse again until you get to the middle


## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLen(self, head):

        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next

        return length

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head
        length = self.getLen(head)
        curLen = 0
        while cur is not None and curLen < length // 2:
            curLen += 1
            cur = cur.next

        return cur

```
