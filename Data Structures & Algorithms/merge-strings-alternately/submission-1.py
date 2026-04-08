class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        res = ""
        while i< len(word1) or j<len(word2):
            curr = ""

            if i<len(word1):
                curr += word1[i]
                i+=1

            if j<len(word2):
                curr+= word2[j]
                j+=1

            res+=curr

        return res