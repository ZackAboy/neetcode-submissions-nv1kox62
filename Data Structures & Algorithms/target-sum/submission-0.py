class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = dict()
        

        def rec(i, bal):
            if i == n:
                if bal == 0:
                    return 1
                return 0

            if (i, bal) not in dp:
                add = rec(i+1, bal+nums[i])
                sub = rec(i+1, bal-nums[i])

                dp[(i, bal)] = add+sub

            return dp[(i, bal)]

        return rec(0, target)