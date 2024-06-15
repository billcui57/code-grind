# Find Median from Data Stream

## Link

https://leetcode.com/problems/find-median-from-data-stream/

## Where

Leetcode

## Difficulty

Hard

## Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

## Solution Main Idea

Have two heaps, one max heap for holding values less than and including median, one minheap for holding values greater than medium. Rebalance to maintain that invariant


## Code

```python
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

```
