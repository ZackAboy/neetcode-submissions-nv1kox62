class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        res = []

        n = len(s)

        def rec(i, path):
            if i == n:
                res.append(path)
                return

            rec(i+1, path)

            path = path + s[i]
            rec(i+1, path)
            path = path[:-1]

        rec(0, "")
        ans = 0
        for c in res:
            if c == t:
                ans+= 1

        return ans
