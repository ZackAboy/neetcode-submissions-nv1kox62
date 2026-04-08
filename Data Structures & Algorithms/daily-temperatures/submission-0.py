class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= []
        for i in range(len(temperatures)):
            dist = 0
            for x in range(i+1, len(temperatures)):
                if temperatures[x] > temperatures[i]:
                    dist = x - i
                    break
            res.append(dist)
        return(res)