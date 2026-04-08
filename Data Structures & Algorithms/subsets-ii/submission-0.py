class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        def rec(i, curr):
            if i == n:
                res.add(tuple(curr))
                return
            
            rec(i+1, curr)
            curr.append(nums[i])
            rec(i+1, curr)
            curr.pop()

        rec(0, [])

        return [list(i) for i in res]