class Solution:

    def floodFill(self, heights, row, col, ocean):
        # assumes already reachable from ocean

        m = len(heights)
        n = len(heights[0])

        if ocean[row][col] is True:
            return ocean[row][col]

        ocean[row][col] = True

        children = []

        if row > 0 and heights[row-1][col] >= heights[row][col]:
            children.append({'row': row-1, 'col': col})
        if row < m-1 and heights[row+1][col] >= heights[row][col]:
            children.append({'row': row+1, 'col': col})
        if col > 0 and heights[row][col-1] >= heights[row][col]:
            children.append({'row': row, 'col': col-1})
        if col < n-1 and heights[row][col+1] >= heights[row][col]:
            children.append({'row': row, 'col': col + 1})

        for child in children:
            self.floodFill(heights, child['row'], child['col'], ocean)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        pacific = [[None] * n for i in range(m)]
        atlantic = [[None] * n for i in range(m)]

        for i in range(m):
            self.floodFill(heights, i, 0, pacific)

        for i in range(n):
            self.floodFill(heights, 0, i, pacific)

        for i in range(m):
            self.floodFill(heights, i, n-1, atlantic)

        for i in range(n):
            self.floodFill(heights, m-1, i, atlantic)

        result = []

        for row in range(m):
            for col in range(n):
                if pacific[row][col] is True and atlantic[row][col] is True:
                    result.append([row, col])

        return result
