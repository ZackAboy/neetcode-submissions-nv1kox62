class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for num in nums:
            count = 1
            while num-1 in nums:
                count+=1
                num-=1
            res = max(res, count)

        return res