class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 0
        p = 0
        while l<len(prices)-1:
            while l<(len(prices)-1) and prices[l]>prices[l+1]:
                l+=1
            r=l
            while r<(len(prices)-1) and prices[r]<prices[r+1]:
                r+=1
            if prices[l]<prices[r]:
                p+= (prices[r] - prices[l])

            l = r
            if l == r:
                l+=1

        return p