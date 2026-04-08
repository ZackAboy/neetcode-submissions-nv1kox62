class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n==1:
            return s

        res = ""

        #odd
        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            if (r-l-1)>len(res):
                res = s[l+1:r]

            l = i
            r = i+1
            while l>=0 and r<n and s[l] == s[r]:
                l-=1
                r+=1
            if (r-l-1)>len(res):
                res = s[l+1:r]

        return res