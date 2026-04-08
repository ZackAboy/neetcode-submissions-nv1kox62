class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        val = 0

        for n in nums:
            if n-1 not in nums:
                curr = n
                currval = 1
                while curr + 1 in nums:
                    currval += 1
                    curr += 1
                val = max(val, currval)
        return val