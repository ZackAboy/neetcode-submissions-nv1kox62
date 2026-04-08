class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for i in range(1, len(strs)):
            j = 0
            while j<len(ans) and j<len(strs[i]) and ans[j] == strs[i][j]:
                j+=1

            ans = ans[:j]
                    
            if ans == "":
                return ""

        return ans