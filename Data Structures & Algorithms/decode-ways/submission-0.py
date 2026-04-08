class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = dict()

        def rec(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0

            if i not in dp:

                res = rec(i+1)

                if (i+1 < n) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                    res += rec(i+2)

                dp[i] = res
            return dp[i]

        return rec(0)


