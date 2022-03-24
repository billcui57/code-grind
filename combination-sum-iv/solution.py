class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:

        A = [0] * (target + 1)

        A[0] = 1

        for amount in range(target+1):
            for num in nums:
                if amount - num >= 0:
                    A[amount] = A[amount - num] + A[amount]

        return A[target]
