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
