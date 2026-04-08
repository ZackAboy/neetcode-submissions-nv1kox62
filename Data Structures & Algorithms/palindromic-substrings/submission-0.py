class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        def palindrome(x):
            l = 0
            r = len(x)-1

            while l<=r:
                if x[l] != x[r]:
                    return False
                l+=1
                r-=1
                
            return True

        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r<len(s) and palindrome(s[l:r+1]) is True:
                count += 1
                l-=1
                r+=1

            l = i
            r = i+1
            while l>=0 and r<len(s) and palindrome(s[l:r+1]) is True:
                count += 1
                l-=1
                r+=1

        return count


                

            