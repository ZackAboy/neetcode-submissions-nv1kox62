class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1freq = [0]*26
        s2freq = [0]*26
        j = len(s1)
        for c in s1:
            s1freq[ord(c)-ord('a')] += 1
        for c in s2[:j]:
            s2freq[ord(c)-ord('a')] += 1
        if s1freq == s2freq:
            return True
        for i in range(1, len(s2)-j+1):
            s2freq[ord(s2[i-1])-ord('a')] -= 1
            s2freq[ord(s2[i+j-1])-ord('a')] += 1
            if s1freq == s2freq:
                return True
        return False