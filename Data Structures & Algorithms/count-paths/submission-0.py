class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = dict()
        dp[(0,0)] = 1

        def rec(r,c):
            if (r, c) not in dp:
                top = left = 0
                if r-1>=0:
                    top = rec(r-1, c)
                if c-1>=0:
                    left = rec(r, c-1)

                dp[(r,c)] = top + left

            return dp[(r,c)]

        return rec(m-1, n-1)
