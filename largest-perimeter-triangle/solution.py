class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        largest = 0

        nums = list(sorted(nums))

        for i in range(2, len(nums)):
            if nums[i-1] + nums[i-2] > nums[i]:
                largest = max(nums[i-1] + nums[i-2] + nums[i], largest)
        return largest
