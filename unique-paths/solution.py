class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        A = [[0] * m] * n

        A[0][0] = 1

        for i in range(1, n):
            A[i][0] = A[i-1][0]

        for j in range(1, m):
            A[0][j] = A[0][j-1]

        for i in range(1, n):
            for j in range(1, m):
                A[i][j] = A[i-1][j] + A[i][j-1]

        return A[n-1][m-1]
