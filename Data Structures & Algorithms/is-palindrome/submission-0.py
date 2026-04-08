class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        l = 0
        r = len(cleaned)-1
        while l<r:
            if cleaned[l] != cleaned[r]:
                return False
            l=l+1
            r=r-1
        return True