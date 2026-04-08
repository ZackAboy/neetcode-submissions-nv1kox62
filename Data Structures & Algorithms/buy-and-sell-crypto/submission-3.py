class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        res = 0

        for n in prices:
            low = min(low, n)
            res = max(res, n-low)

        return res