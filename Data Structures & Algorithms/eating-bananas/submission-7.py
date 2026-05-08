class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def bananer(x):
            ans = 0
            for val in piles:
                ans += math.ceil(val/x)
            return ans

        l = 1
        r = max(piles)
        res = float('inf')

        while l<=r:
            mid = (l+r)//2
            curr = bananer(mid)

            if curr > h:
                l = mid + 1

            elif curr <=h :
                res = min(res, mid)
                r = mid - 1

        return res