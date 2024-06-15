# Top K Frequent Elements

## Link

https://leetcode.com/problems/top-k-frequent-elements/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Solution Main Idea

Get list of freq, heapify into max heap and then heap pop the first k


## Code

```python
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        heap = []

        for num in freq:
            heap.append(
                (-1 * freq[num], num)
            )  # -1 because heapq uses minheap, we want max heap

        heapq.heapify(heap)

        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result

```
