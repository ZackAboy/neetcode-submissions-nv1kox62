class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = defaultdict(int)
        ht = defaultdict(int)

        for c in s:
            hs[c] += 1
        
        for c in t:
            ht[c] += 1

        return hs == ht