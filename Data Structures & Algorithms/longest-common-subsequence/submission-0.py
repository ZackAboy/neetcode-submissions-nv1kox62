class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = dict()
        m = len(text1)
        n = len(text2)

        def rec(i, j):
            if i==m or j==n:
                return 0
            if (i, j) not in dp:
                if text1[i] == text2[j]:
                    dp[(i, j)] = rec(i+1, j+1) + 1
                else:
                    dp[(i, j)] = max(rec(i+1, j), rec(i, j+1))
            return dp[(i, j)]

        return rec(0,0)