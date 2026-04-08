class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        curr = defaultdict(int)
        need = len(target)
        have = 0
        minl = float('inf')
        res = ""
        l = 0

        for r in range(len(s)):
            curr[s[r]]+=1
            if s[r] in target and target[s[r]] == curr[s[r]]:
                have += 1
            while have == need:
                if minl > (r-l+1):
                    res = s[l:r+1]
                    minl = min(minl, (r-l+1))
                curr[s[l]]-=1
                if s[l] in target and curr[s[l]] < target[s[l]]:
                    have -= 1
                l+=1
        return res