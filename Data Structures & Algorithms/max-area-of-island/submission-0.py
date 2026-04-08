class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        li = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j] == 0:
                return None

            self.area += 1
            grid[i][j] = 0

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    li = max(li, self.area)
        return li