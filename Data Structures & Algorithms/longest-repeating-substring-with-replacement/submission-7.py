class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq = defaultdict(int)
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            most = max(freq.values())
            while sum(freq.values()) > most + k:
                freq[s[l]] -= 1
                l+=1
            res = max(res, (r-l+1))
        return res