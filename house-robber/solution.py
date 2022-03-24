class Solution:
    def rob(self, nums: List[int]) -> int:

        A = [-inf] * len(nums)

        A[0] = nums[0]

        for houseIndex in range(1, len(nums)):
            if houseIndex - 2 >= 0:
                A[houseIndex] = max(nums[houseIndex] +
                                    A[houseIndex-2], A[houseIndex - 1])
            else:
                A[houseIndex] = max(nums[houseIndex], A[houseIndex - 1])

        return A[len(nums) - 1]
