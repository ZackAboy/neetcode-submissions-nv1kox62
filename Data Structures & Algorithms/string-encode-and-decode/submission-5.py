class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            n = str(n)
            res += n + "@" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        r = 0
        res = []
        while r < (len(s)):
            l = r
            while s[r] != "@":
                r+=1
            n = int(s[l:r])
            r += 1 + n
            l = r - n
            res.append(s[l:r])
        return res