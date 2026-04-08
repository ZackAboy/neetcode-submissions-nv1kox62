class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def recur(visited, curr):
            if len(curr) == n:
                res.append(curr.copy())

            for num in nums:
                if num not in visited:
                    visited.add(num)
                    curr.append(num)
                    recur(visited, curr)
                    visited.remove(num)
                    curr.pop()

        recur(set(), [])
        return res