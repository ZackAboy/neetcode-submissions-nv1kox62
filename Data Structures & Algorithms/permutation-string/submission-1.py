class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = [0]*26
        for c in s1:
            s1freq[ord(c)-ord('a')] += 1
        j = len(s1)
        for i in range(len(s2)-j+1):
            s2freq = [0]*26
            for c in s2[i:i+j]:
                s2freq[ord(c)-ord('a')] += 1
            if s1freq == s2freq:
                return True
        return False