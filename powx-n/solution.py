class Solution:

    def DP(self, x, n ,memo):
        if n in memo:
            return memo[n]
        if n == 1:
            memo[1] = x
            return x
        if n == 0:
            memo[0] = 1
            return 1
        if n < 0:
            return 1/(self.DP(x, -1 * n,memo))
        
        
        result =self.DP(x,ceil(n/2),memo) * self.DP(x,floor(n/2),memo)
        memo[n] = result
        return result
    def myPow(self, x: float, n: int) -> float:
        return self.DP(x,n,dict())
