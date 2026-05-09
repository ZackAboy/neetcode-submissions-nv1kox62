class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = Counter(s1)
        l = 0
        for r in range(len(s1), len(s2)+1):
            if Counter(s2[l:r]) == check:
                return True
            l+=1
        return False