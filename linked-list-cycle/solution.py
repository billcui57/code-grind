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
