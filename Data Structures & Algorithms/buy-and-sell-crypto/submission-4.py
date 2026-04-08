class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying = float('inf')

        for num in prices:
            buying = min(buying, num)
            profit = max(profit, num - buying)

        return profit