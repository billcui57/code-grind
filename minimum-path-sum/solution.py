class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows= len(grid)
        cols = len(grid[0])
        cost = [[0] * cols for i in range(rows)]

        cost[0][0] = grid[0][0]

        for row in range(1,rows):
            cost[row][0] = cost[row-1][0] + grid[row][0]
        
        for col in range(1, cols):
            cost[0][col] = cost[0][col-1] + grid[0][col]
        
        for row in range(1, rows):
            for col in range(1,cols):
                cost[row][col] = grid[row][col]+ min(cost[row-1][col], cost[row][col-1])
        return cost[rows-1][cols-1]
            
