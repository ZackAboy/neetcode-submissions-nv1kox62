class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            s = str(len(s)) + "$" + s
            res.append(s)
        s = "".join(res)
        return s
            
    def decode(self, s: str) -> List[str]:
        l = 0
        res = []
        while l<len(s):
            chars = []
            while s[l] != "$":
                chars.append(s[l])
                l += 1
            k = int("".join(chars))
            word = []
            l += 1
            while k>0:
                word.append(s[l])
                l += 1
                k -= 1
            res.append("".join(word))
        return res