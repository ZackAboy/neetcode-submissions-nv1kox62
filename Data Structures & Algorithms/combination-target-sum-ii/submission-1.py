class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def comb(start, curr, val):
            if val >= target:
                if val == target:
                    res.append(curr.copy())
                return

            for i in range(start, n):
                if i> start and candidates[i] == candidates[i-1]:
                    continue
                curr.append(candidates[i])
                comb(i+1, curr, val + candidates[i])
                curr.pop()
        comb(0, [], 0)
        return res