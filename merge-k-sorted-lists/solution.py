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
