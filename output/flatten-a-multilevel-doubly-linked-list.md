# Flatten a Multilevel Doubly Linked List

## Link

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/

## Where

Leetcode

## Difficulty

Medium

## Description

You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

## Solution Main Idea

Recurse on child nodes. Get recursion result and splice it into current linked list. Return last node of current linked list for splicing.


## Code

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

#       1,2,3,4,5,6,null
# null,null,7,8,null
#        null,11,12
class Solution:

    def helper(self, head):
        node = head
        prevNode = None
        while node is not None:
            if node.child is not None:
                child_end = self.helper(node.child)
                if node.next is not None:
                    temp = node.next
                    node.next = node.child
                    child_end.next = temp
                    temp.prev = child_end
                    node.child.prev = node
                else:
                    temp = node.child
                    node.next = temp
                    temp.prev = node
                node.child = None
                prevNode = child_end #we can avoid traversing through the list by jumping directly to the end of the child node
                node = child_end.next
            else:
                prevNode = node
                node = node.next
        return prevNode

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.helper(head)
        return head


```
