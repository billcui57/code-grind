import heapq


class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
        return

    def addNum(self, num: int) -> None:
        # we multiply by -1 to turn heapq's minheap to maxheap for left

        if len(self.left) == 0 or num <= -1 * self.left[0]:
            heapq.heappush(self.left, -1 * num)
        else:
            heapq.heappush(self.right, num)

        if len(self.right) > len(self.left):
            item = heapq.heappop(self.right)
            heapq.heappush(self.left, -1 * item)

        if len(self.left) > len(self.right) + 1:
            item = heapq.heappop(self.left)
            heapq.heappush(self.right, -1 * item)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (-1 * self.left[0] + self.right[0]) / 2
        return -1 * self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
