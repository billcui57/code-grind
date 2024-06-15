# Merge k Sorted Lists

## Link

https://leetcode.com/problems/merge-k-sorted-lists/

## Where

Leetcode

## Difficulty

Hard

## Description

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

## Solution Main Idea

Use a min heap PQ that holds the heads of all linked lists. Pop the head from the top of the PQ and append it to the back of the new linked list. Add the next of head back into PQ. Continue until PQ is empty


## Code

```python
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        largest_queue = []

        for list in lists:
            if list:
                heapq.heappush(largest_queue, (list.val, id(list), list))

        newList = None
        oldList = None
        returnList = None

        while len(largest_queue) > 0:

            newList = ListNode()

            if oldList:
                oldList.next = newList
            else:
                returnList = newList

            largest = heapq.heappop(largest_queue)

            if largest[2].next:
                heapq.heappush(
                    largest_queue,
                    (largest[2].next.val, id(largest[2].next), largest[2].next),
                )

            newList.val = largest[0]

            oldList = newList
        return returnList

```
