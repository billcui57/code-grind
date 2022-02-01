from typing import List


class Solution:
    def getMaxMidSubarray(self, start, end, mid, nums):

        maxLeftSum = -1000000000
        currLeftSum = 0
        includeLeft = False

        for i in reversed(range(start, mid+1)):
            currLeftSum += nums[i]
            if currLeftSum >= maxLeftSum:
                includeLeft = True
                maxLeftSum = currLeftSum

        maxRightSum = -1000000000
        currRightSum = 0
        includeRight = False

        for i in range(mid+1, end+1):
            currRightSum += nums[i]
            if currRightSum >= maxRightSum:
                includeRight = True
                maxRightSum = currRightSum

        print(maxLeftSum)
        print(maxRightSum)

        result = 0

        if includeLeft:
            result += maxLeftSum
        if includeRight:
            result += maxRightSum

        return result

    def DoC(self, start, end, nums):
        if start >= end:
            return nums[start]

        mid = (int)((start + end) / 2)

        maxSubArrayLeft = self.DoC(start, mid, nums)
        maxSubArrayRight = self.DoC(mid+1, end, nums)
        maxSubArrayBetween = self.getMaxMidSubarray(start, end, mid, nums)


        return max(maxSubArrayLeft, maxSubArrayRight, maxSubArrayBetween)

    def maxSubArray(self, nums: List[int]) -> int:
        return self.DoC(0, len(nums)-1, nums)



