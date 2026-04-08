class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        l = 0
        r = 1
        profit = 0
        while r in range(len(prices)):
            if prices[r] <= prices[l]:
                l = r
            else:
                if (prices[r] - prices[l])>profit:
                    profit = (prices[r]-prices[l])
            r += 1
        return profit