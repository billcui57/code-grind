# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oldHead = None
        newHead = None
        while head:
            newHead = ListNode(val=head.val)
            if oldHead:
                newHead.next = oldHead
            head = head.next
            oldHead = newHead

        return newHead
