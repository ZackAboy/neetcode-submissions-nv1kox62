from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for string in strs:
            letters = [0]*26

            for character in string:
                letters[ord(character)-ord('a')] += 1

            key = tuple(letters)
            ans[key].append(string)

        return list(ans.values())