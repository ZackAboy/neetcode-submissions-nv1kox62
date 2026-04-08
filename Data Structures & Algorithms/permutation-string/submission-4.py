class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        l = 0
        target = [0]*26
        for c in s1:
            index = ord(c) - ord('a')
            target[index] += 1

        for r in range(n, m+1):
            curr = [0]*26
            for c in s2[l:r]:
                index = ord(c) - ord('a')
                curr[index] += 1
            if curr == target:
                return True
            l+=1

        return False