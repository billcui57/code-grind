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

