class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        move = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    count+=1
                    stack = [(r,c)]
                    while stack:
                        row, col = stack.pop()
                        grid[row][col] = "-1"
                        for i, j in move:
                            nr, nc = row+i, col+j
                            if 0<=nr<m and 0<=nc<n and grid[nr][nc] == "1":
                                stack.append((nr,nc))

        return count
