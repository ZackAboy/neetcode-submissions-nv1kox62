class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n==1:
            return nums[0]

        def rob1(x):
            m = len(x)

            dp = dict()
            
            def rec(i):
                if i >= m:
                    return 0

                if i not in dp:

                    dp[i] = max(rec(i+2)+x[i], rec(i+1))

                return dp[i]

            return rec(0)

        return max(rob1(nums[:n-1]), rob1(nums[1:n]))