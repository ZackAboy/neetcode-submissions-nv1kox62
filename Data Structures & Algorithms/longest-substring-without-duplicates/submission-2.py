class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        l = 0
        res = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l +=1
            seen.add(s[r])
            if (r-l)> res:
                res = (r-l)
        return res+1