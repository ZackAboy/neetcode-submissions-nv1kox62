class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            j = i+1
            k = len(nums)-1
            while j<k:
                x = (nums[i], nums[j], nums[k])
                val = sum(x)
                if val == 0:
                    res.add(x)
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1

                elif val>0:
                    k-=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                else:
                    j+=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
            
        return list(res)

