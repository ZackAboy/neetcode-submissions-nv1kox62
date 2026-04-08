class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = dict()

        def rec(i, bal):
            if bal<0 or i==n:
                return 0
            if bal == 0:
                return 1
            if (i, bal) not in dp:
                take = rec(i, bal - coins[i])
                skip = rec(i+1, bal)

                dp[(i, bal)] = take + skip

            return dp[i, bal]

        return rec(0, amount)
                
                    