class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1sort = sorted(s1)
        print (s1sort)
        j = len(s1)
        for i in range((len(s2)-j)+1):
            s2sort = sorted(s2[i:i+j])
            print(s2sort)
            if s2sort == s1sort:
                return True
        return False