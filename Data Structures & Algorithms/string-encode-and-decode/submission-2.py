class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            x = len(s)
            res = res + str(x) + "@" + s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        digits = "0123456789"

        while i<len(s):
            x = ""
            while s[i] in digits:
                x = x + s[i]
                i+= 1

            if s[i] == "@":
                i+=1
                c = ""
                for _ in range(int(x)):
                    c = c + s[i]
                    i+=1
                res.append(c)
        
        return res
