class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for string in strs:
            val = [0]*26
            for c in string:
                i = ord("a")-ord(c)
                val[i] += 1
            if tuple(val) in res:
                res[tuple(val)].append(string)
            else:
                res[tuple(val)] = [string]

        return [i for i in res.values()]