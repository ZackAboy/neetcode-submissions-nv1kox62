class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def visitor():
            count = 1
            while stack:
                l = stack.pop()
                i = l[0]
                j = l[1]
                if i+1 < m and grid[i+1][j] == 1:
                    grid[i+1][j] = 0
                    stack.append([i+1, j])
                    count += 1
                if i-1 > -1 and grid[i-1][j] == 1:
                    grid[i-1][j] = 0
                    stack.append([i-1, j])
                    count += 1
                if j+1 < n and grid[i][j+1] == 1:
                    grid[i][j+1] = 0
                    stack.append([i, j+1])
                    count += 1
                if j-1 > -1 and grid[i][j-1] == 1:
                    grid[i][j-1] = 0
                    stack.append([i, j-1])
                    count += 1
            return count
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range (m):
            for j in range (n):
                stack = []
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    stack.append([i, j])
                    res = max(res, visitor())
        return res
