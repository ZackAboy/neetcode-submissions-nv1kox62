class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = dict()
        for i, num in enumerate(nums):
            val = target - num
            if val in comp:
                return [comp[val], i]
            comp[num] = i