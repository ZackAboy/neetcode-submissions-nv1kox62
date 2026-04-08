import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = math.inf
        while l <= r:
            mid = (l + r)//2
            total = 0
            for i in piles:
                if (i%mid) == 0:
                    total = total + (i//mid)
                else:
                    total = total +(i//mid) + 1
            if total <= h:
                if mid < res:
                    res = mid
                r = mid -1
            elif total > h:
                l = mid + 1
        return res