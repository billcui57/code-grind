class Solution:



    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[inf] * n for i in range(m)]

        queue = []
        seen= set()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col,0))
                    result[row][col] = 0
                    seen.add((row,col))
        
        
        while len(queue) > 0:
            row,col,distFromZero = queue.pop(0)
       
            result[row][col] = distFromZero

            neighbours = []

            if row - 1 >= 0:
                neighbours.append((row-1,col))
            if row + 1 <= m-1:
                neighbours.append((row+1, col))
            if col - 1 >= 0:
                neighbours.append((row, col-1))
            if col + 1 <= n-1:
                neighbours.append((row, col+1))
            
           
            for neighbour in neighbours:
                nrow,ncol = neighbour
                if (nrow,ncol) not in seen:
                    result[nrow][ncol] = distFromZero + 1
                    queue.append((nrow, ncol,distFromZero+1))
                    seen.add((nrow,ncol))
        return result

        