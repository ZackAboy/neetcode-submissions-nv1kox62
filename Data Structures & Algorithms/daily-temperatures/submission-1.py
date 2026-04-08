class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = list(enumerate(temperatures))
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if stack ==[]:
                stack.append(temperatures[i])
            else:
                if temperatures[i][1] <= stack[-1][1]:
                    stack.append(temperatures[i])
                while stack and temperatures[i][1] > stack[-1][1]:
                    res[stack[-1][0]] = temperatures[i][0] - stack[-1][0]
                    stack.pop()
                stack.append(temperatures[i])
        return(res)