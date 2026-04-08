class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        while x in range (len(nums)):
            y=x+1
            while y in range(len(nums)):
                if nums[x]+nums[y]==target:
                    return[x,y]
                else:
                    y=y+1
            x=x+1
