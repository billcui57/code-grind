class Solution:
    def canJump(self, nums: List[int]) -> bool:

        A = [0] * (len(nums)-1)

        if len(nums) == 1:
            return True

        for i in range(len(nums)-1):
            if A[i-1] >= i:
                A[i] = max(A[i-1], i + nums[i])

        return A[-1] >= (len(nums) - 1)
