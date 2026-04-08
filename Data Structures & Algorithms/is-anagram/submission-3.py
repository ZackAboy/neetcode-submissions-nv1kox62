class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = [0]*26
        for i in s:
            res[(ord(i.lower()) - ord('a'))] += 1
        for i in t:
            if res[(ord(i.lower()) - ord('a'))] > 0:
                res[(ord(i.lower()) - ord('a'))] -= 1
            else:
                return False
        return True