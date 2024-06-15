# Reorder List

## Link

https://leetcode.com/problems/reorder-list/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Solution Main Idea

Three steps. Find middle node, reverse list at middle node, reorder by alternate setting heads


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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find middle
        slow = head
        fast = head
        while slow and fast and slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow

        # reverse middle
        reversedMiddle = self.reverseList(middle)

        # reorder
        p1 = head
        p2 = reversedMiddle
        p1Next = None
        while p1 and p2 and p1.next:
            p1Next = p1.next
            p1.next = p2
            p1 = p2
            p2 = p1Next

        return head

```
