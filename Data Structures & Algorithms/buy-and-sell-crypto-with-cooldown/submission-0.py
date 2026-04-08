class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = dict()

        def rec(i, hold):
            if i >= n:
                return 0
            if (i, hold) not in dp:
                if hold == True:
                    sell = prices[i] + rec(i+2, False)
                    skip = rec(i+1, True)
                    dp[(i, hold)] = max(sell, skip)
                else:
                    buy = rec(i+1, True) - prices[i]
                    skip = rec(i+1, False)
                    dp[(i, hold)] = max(buy, skip)
            return dp[(i, hold)]

        return rec(0,False)