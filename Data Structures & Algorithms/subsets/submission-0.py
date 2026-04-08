class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def subset(i, curr):
            if i == n:
                res.append(curr.copy())
                return

            
            subset(i+1, curr)
            curr.append(nums[i])
            subset(i+1, curr)
            curr.pop()

        subset(0, [])

        return res