class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visitor():
            while stack:
                l = stack.pop()
                i = l[0]
                j = l[1]
                grid[i][j] = "0"
                if i+1<m and grid[i+1][j] == "1":
                    stack.append([i+1, j])
                if i-1>-1 and grid[i-1][j] == "1":
                    stack.append([i-1, j])
                if j+1<n and grid[i][j+1] == "1":
                    stack.append([i, j+1])
                if j-1>-1 and grid[i][j-1] == "1":
                    stack.append([i, j-1])

        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range (m):
            for j in range (n):
                stack = []
                if grid[i][j] == "1":
                    stack.append([i, j])
                    count += 1
                    visitor()
        return count