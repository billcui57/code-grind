# Remove Nth Node From End of List

## Link

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## Where

Leetcode

## Difficulty

Medium

## Description

Given the head of a linked list, remove the nth node from the end of the list and return its head.

## Solution Main Idea

Use tail recursion to get a node's location relative to the end of the list. Remove if its location is $n$


## Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEndHelper(
        self, head: Optional[ListNode], n: int, prev
    ) -> Optional[ListNode]:

        if head is None:
            return 1, head

        location = self.removeNthFromEndHelper(head.next, n, head)[0]
        print(str(location) + "\t" + str(head.val))
        if location == n:
            if prev:
                prev.next = head.next
            else:
                head = head.next
        return (
            location + 1,
            head,
        )
        # We return head in the case we are removing the first node in the list,
        # the main function still holds reference to the old head so we need to
        # return the new head to update it

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        head = self.removeNthFromEndHelper(head, n, None)[1]

        return head

```
