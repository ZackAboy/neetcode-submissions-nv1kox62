class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = dict()

        move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def rec (r, c):
            if (r, c) not in dp:
                best = 1
                for i,j in move:
                    nr, nc = r+i, c+j

                    if nr<m and nr>=0 and nc<n and nc>=0 and matrix[nr][nc] > matrix[r][c]:
                        best = max(best, rec(nr, nc)+1)

                dp[(r, c)] = best
            return dp[(r, c)]

        res = 0
        for r in range(m):
            for c in range(n):
                res = max(res, rec(r, c))

        return res