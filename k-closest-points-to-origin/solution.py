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

        