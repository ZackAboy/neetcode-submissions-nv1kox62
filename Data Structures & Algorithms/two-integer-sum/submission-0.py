class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        res=[]
        while x in range (len(nums)):
            y=x+1
            while y in range(len(nums)):
                if nums[x]+nums[y]==target:
                    res.append(x)
                    res.append(y)
                    return(res)
                else:
                    y=y+1
            x=x+1
