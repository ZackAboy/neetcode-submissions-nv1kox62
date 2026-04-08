class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = dict()
        dp[0] = 0

        def rec(bal):
            if bal not in dp:
                best = float('inf')
                for c in coins:
                    if bal - c >= 0:
                        best = min(best, rec(bal-c) + 1)
                dp[bal] = best
            return dp[bal]

        return rec(amount) if rec(amount) != float('inf') else -1
                    