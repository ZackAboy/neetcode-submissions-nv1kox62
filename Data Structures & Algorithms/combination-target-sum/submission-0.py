class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)

        def comb(i, curr, total):
            if i == n or total>=target:
                if total == target:
                    res.append(curr.copy())
                return

            comb(i+1, curr, total)
            curr.append(nums[i])
            comb(i, curr, total+nums[i])
            curr.pop()

        comb(0, [], 0)
        return res