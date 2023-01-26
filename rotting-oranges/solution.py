class Solution:

    def findRotting(self,grid):
        m = len(grid)
        n = len(grid[0])

        rottingPos=set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    rottingPos.add((row,col))
        return rottingPos

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        seen = set()

        minDistance = [[-1] * n for i in range(m)] 

        rottingOranges = self.findRotting(grid)
        queue = [(rottingOrangePos, 0) for rottingOrangePos in rottingOranges]
        seen = rottingOranges

        while len(queue) > 0:
            pos,distance = queue.pop(0)
            row,col = pos

            minDistance[row][col] = distance

            neighbours = []
            if row + 1 <= m-1:
                neighbours.append((row+1, col))
            if row - 1 >=0:
                neighbours.append((row -1,col))
            if col + 1 <= n-1:
                neighbours.append((row, col+1))
            if col - 1 >= 0:
                neighbours.append((row, col-1))
            
            for neighbour in neighbours:
                nrow,ncol = neighbour
                if neighbour not in seen and grid[nrow][ncol] != 0:
                    seen.add(neighbour)
                    queue.append((neighbour, distance + 1))
        
        # print(minDistance)
        maxRotDistance = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] != 0:
                    if minDistance[row][col] == -1:
                        return -1
                    maxRotDistance = max(maxRotDistance,minDistance[row][col])
        return maxRotDistance

            
            
