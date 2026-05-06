class Solution:
    def trap(self, height: List[int]) -> int:
        l = res = lmax = rmax = 0
        r = len(height) - 1
        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if height[l] < height[r]:
                curr = min(lmax, rmax) - height[l]
                l+=1
            
            else:
                curr = min(lmax, rmax) - height[r]
                r-=1
            
            res += curr if curr>0 else 0

        return res