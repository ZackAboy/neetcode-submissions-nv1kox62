class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        n = len(nums)
        postfix = [0]*n
        for i in range(n-1, -1, -1):
            postfix[i] = prev
            prev*= nums[i]
        prev = 1
        for i in range(n):
            postfix[i]*=prev
            prev*= nums[i]

        return postfix