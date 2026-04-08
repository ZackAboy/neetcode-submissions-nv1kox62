class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            n = len(s)
            n = str(n)
            res += n + "@" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        l = 0
        r = 0
        res = []
        while r < (len(s)):
            while s[r] != "@":
                r+=1
            n = int(s[l:r])
            r += 1 + n
            l = r - n
            res.append(s[l:r])
            l = r

        return res