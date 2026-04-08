class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        seen = set(nums)
        for i in seen:
            if i-1 not in seen:
                j = i
                count = 1
                while j+1 in seen:
                    count += 1
                    j += 1
                res = max(res, count)
        return res