class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for string in strs:
            val = [0]*26
            for c in string:
                i = ord(c)-ord("a")
                val[i] += 1
            key = tuple(val)
            if key in res:
                res[key].append(string)
            else:
                res[key] = [string]

        return [i for i in res.values()]