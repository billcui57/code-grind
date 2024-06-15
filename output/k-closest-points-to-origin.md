# K Closest Points to Origin

## Link

https://leetcode.com/problems/k-closest-points-to-origin/description/

## Where

Leetcode

## Difficulty

Medium

## Description

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

## Solution Main Idea

Use quick select to find index of k smallest


## Code

```python
import random
class Solution:
    def euclidDist(self,val):
        return val[0] ** 2+ val[1] ** 2

    def partition(self,arr,lo,hi):
        pivotIndex = random.randint(lo,hi)
        arr[pivotIndex], arr[hi] = arr[hi], arr[pivotIndex]

        pivot = self.euclidDist(arr[hi])
        i = lo 
        for j in range(lo,hi):
            if self.euclidDist(arr[j]) <= pivot:
                arr[i],arr[j] = arr[j],arr[i]
                i+=1
        arr[i],arr[hi] = arr[hi],arr[i]
        return i

    def quickSelect(self,arr,lo,hi,k):
        if not (k > 0 and k <= hi - lo + 1):
            return lo
        pivotIndex = self.partition(arr, lo,hi)
        if pivotIndex-lo == k-1:
            return pivotIndex
        if pivotIndex-lo < k-1:
            return self.quickSelect(arr,pivotIndex+1, hi,   k - (pivotIndex - lo + 1))
        return self.quickSelect(arr, lo, pivotIndex-1,k)

        

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        kthSmallestIndex = self.quickSelect(points, 0, len(points)-1, k)
        return points[0:kthSmallestIndex+1]

        
```
