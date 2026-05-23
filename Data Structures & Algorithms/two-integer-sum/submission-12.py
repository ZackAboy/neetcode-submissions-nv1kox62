class Solution:
    def twoSum(self, nums, target):
        comp = dict()
        for i, num in enumerate(nums):
            val = target - num
            if val in comp:
                return [comp[val], i]
            comp[num] = i