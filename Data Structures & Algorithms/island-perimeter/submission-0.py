class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        m = len(grid)
        p = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    p += 4
                    if i>0 and grid[i-1][j] == 1:
                        p -= 1
                    if i<m-1 and grid[i+1][j] == 1:
                        p -= 1
                    if j>0 and grid[i][j-1] == 1:
                        p -= 1
                    if j<n-1 and grid[i][j+1] == 1:
                        p -= 1
        return p