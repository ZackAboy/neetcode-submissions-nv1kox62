class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustin = [0]*(n+1)
        trustout = [0]*(n+1)

        for i in range (len(trust)):
            trustout[trust[i][0]]+=1
            trustin[trust[i][1]]+=1

        for i in range(1, n+1):
            if trustin[i] == n-1:
                if trustout[i] == 0:
                    return i

        return -1

