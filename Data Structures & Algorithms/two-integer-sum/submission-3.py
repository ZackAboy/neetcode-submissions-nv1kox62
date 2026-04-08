class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in hash:
                return [hash[x], i]
            hash[n] = i