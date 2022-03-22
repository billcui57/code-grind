class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        A = [1] * len(nums)

        currMax = 1

        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    A[i] = max(A[i], A[j]+1)

                if A[i] > currMax:
                    currMax = A[i]

        return currMax
