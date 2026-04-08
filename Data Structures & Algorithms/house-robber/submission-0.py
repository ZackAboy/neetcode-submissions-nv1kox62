class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]

        dp = dict()
        
        def rec(i):
            if i >= n:
                return 0

            if i not in dp:

                dp[i] = max(rec(i+2)+nums[i], rec(i+1))

            return dp[i]

        return rec(0)