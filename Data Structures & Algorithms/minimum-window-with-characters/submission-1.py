class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        curr = defaultdict(int)
        need = len(set(t))
        have = 0

        l = 0
        res = ""
        for r in range(len(s)):
            curr[s[r]] += 1
            if s[r] in target and target[s[r]] == curr[s[r]]:
                have += 1

            while have == need:
                if res == "":
                    res = s[l:r+1]
                elif len(res) > r-l+1:
                    res = s[l:r+1]
                curr[s[l]] -= 1
                if s[l] in target and curr[s[l]]<target[s[l]]:
                    have -=1
                l+=1
        
        return res