class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0]*n
        for i in range(n):
            val = temperatures[i]
            if not stack or val < stack [-1][0]:
                stack.append((val,i))
            else:
                while stack and stack[-1][0]<val:
                    x, idx = stack.pop()
                    res[idx] = i - idx
                stack.append((val, i))
        return res