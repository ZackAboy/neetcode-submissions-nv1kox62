class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1 = cost[1]
        c2 = cost[0]

        n = len(cost)

        if n <= 2:
            return min(c1, c2)

        for i in range(2, n):
            total = min(c1,c2)+ cost[i]
            c2 = c1
            c1 = total

        return min(c1, c2)