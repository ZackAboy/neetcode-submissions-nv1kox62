class Solution:
    def trap(self, height: List[int]) -> int:
        hd = max(height)
        size = 0
        for i in range (hd):
            l = 0
            r = len(height) - 1
            while l<r and height[l] <= i:
                l += 1
            while l<r and height[r] <= i:
                r -= 1
            for j in range (l, r):
                if height[j]<=i:
                    size += 1
        print(size)
        return(size)
