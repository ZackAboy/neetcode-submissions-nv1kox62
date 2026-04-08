class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = dict()

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in comp:
                return ([comp[rem], i])
            comp[nums[i]] = i