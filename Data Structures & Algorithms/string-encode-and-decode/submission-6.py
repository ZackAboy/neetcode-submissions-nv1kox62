class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        r = 0
        while r < len(s):
            l = r
            while r < len(s) and s[r] != "#":
                r+=1
            x = int(s[l:r])
            l = r+1
            r = l+x
            res.append(s[l:r])
        return res