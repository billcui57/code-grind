class Solution:
    def climbStairs(self, n: int) -> int:

        totalSteps = [0] * (n+1)

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        totalSteps[len(totalSteps)-1] = 0
        totalSteps[len(totalSteps)-2] = 1
        totalSteps[len(totalSteps)-3] = 2

        for i in reversed(range(len(totalSteps)-3)):
            totalSteps[i] = totalSteps[i+1] + totalSteps[i+2]

        return totalSteps[0]
