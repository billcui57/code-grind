class Solution:

    def get_min(self,nums):
        lo = 0
        hi = len(nums)-1

        while lo < hi:
            if nums[lo] < nums[hi]: #array has no shift
                return lo
            
            middle = (lo + hi)//2

            if nums[middle] > nums[middle+1]: #pivot is at middle +1
                return middle+1
            

            if nums[lo] < nums[middle]: #pivot is to the right
                lo = middle+1
                continue
            if nums[lo] > nums[middle]: #pivot is to the left
                hi = middle
                continue
        return hi
    


            
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.get_min(nums)
        lo = 0
        hi = len(nums)-1
        def mapper(index):
            return (min_index+index)%len(nums)
        while lo <= hi:
            middle = (lo + hi)//2
            if target < nums[mapper(middle)]:
                hi = middle-1
                continue
            if target > nums[mapper(middle)]:
                lo = middle+1
                continue
            return mapper(middle)
        return -1
                


