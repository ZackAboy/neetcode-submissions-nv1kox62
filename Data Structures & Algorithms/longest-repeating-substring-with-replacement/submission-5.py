class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = 0
        count = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            f = max(f, count[s[r]])
            while (r-l+1) - f > k:
                count[s[l]] -= 1
                l+=1

            res = max(res, r-l+1)
        return res
