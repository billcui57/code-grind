# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        head = 1
        tail = n

        while head < tail:
            middle = (head + tail) // 2

            if isBadVersion(middle):
                tail = middle
            else:
                head = middle + 1

        return head
