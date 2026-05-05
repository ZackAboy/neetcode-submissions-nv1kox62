class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1]*n

        for i in range(n-2, -1, -1):
            res[i] = res[i+1]*nums[i+1]

        prev = 1
        for i in range(n):
            res[i] *= prev
            prev *= nums[i]

        return res