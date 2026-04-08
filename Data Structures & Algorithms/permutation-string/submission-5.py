class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        l = 0
        target = [0]*26
        for c in s1:
            index = ord(c) - ord('a')
            target[index] += 1

        curr = [0]*26
        for r in range(m):
            if r>=n:
                index = ord(s2[l]) - ord('a')
                curr[index] -=1
                l+=1
            index = ord(s2[r]) - ord('a')
            curr[index] +=1
            if curr == target:
                return True
                
        return False