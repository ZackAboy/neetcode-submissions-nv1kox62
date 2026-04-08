class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        res = 0
        left = 0
        right = 0
        while l<r:
            left = max(left, height[l])
            right = max(right, height[r])
            if height[l] >height[r]:
                curr = min(left, right) - height[r]
                r-=1
            else:
                curr = min(left, right) - height[l]
                l+=1
            
            res+= curr if curr>0 else 0

        return res