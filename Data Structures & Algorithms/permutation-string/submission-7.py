class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = [0]*26
        curr = [0]*26
        for c in s1:
            check[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            curr[ord(s2[r]) - ord('a')] += 1

            if (r-l+1) > len(s1):
                curr[ord(s2[l]) - ord('a')] -= 1
                l+=1
            
            if curr == check:
                return True

        return False