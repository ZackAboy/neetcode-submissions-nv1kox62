class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findtime(mid):
            time = 0
            for num in piles:
                    time += -(-num//mid)
            return time

        l, r = 1, max(piles)
        if len(piles) == h:
            return r
        best = float('inf')
        while l <=r:
            mid = (r+l)//2

            if findtime(mid)<= h:
                r = mid-1
                best = min(best, mid)

            else:
                l = mid+1

        return best
