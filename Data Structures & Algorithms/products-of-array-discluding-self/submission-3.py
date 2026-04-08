class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix = [1] * n
        post = 1
        for i in range(n-1, -1, -1):
            postfix[i] = post
            post*=nums[i]

        prefix = 1
        res = [0]*n
        for i in range(n):
            val = prefix * postfix[i]
            res[i] = val
            prefix*=nums[i]
        return res