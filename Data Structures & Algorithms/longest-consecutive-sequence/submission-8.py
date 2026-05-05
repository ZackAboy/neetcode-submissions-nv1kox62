class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num + 1 in nums:
                continue
            curr = 0
            while num - 1 in nums:
                num -= 1
                curr += 1
            res = max(res, curr+1)

        return res