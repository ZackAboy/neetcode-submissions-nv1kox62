class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l = 0
        r = len(s) - 1

        while l<r:
            if s[l] != s[r]:
                if pal(l+1, r) or pal(l, r-1):
                    return True
                return False
            l+=1
            r-=1

        return True