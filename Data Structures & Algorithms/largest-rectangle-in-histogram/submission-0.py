class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i,val in enumerate(heights):
            if not stack or val > stack[-1][1]:
                stack.append((i, val))

            elif val == stack[-1][1]:
                stack.append(stack[-1])

            else:
                while stack and stack[-1][1] > val:
                    idx, h = stack.pop()
                    res = max(res, (i-idx)*h)
                
                stack.append((idx, val))

        i = len(heights)
        while stack:
            idx, h = stack.pop()
            res = max(res, (i-idx)*h)

        return res