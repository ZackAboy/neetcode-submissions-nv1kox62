class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for s in strs:
            val = [0] * 26
            for c in s:
                index = ord('a') - ord(c)
                val[index] += 1
            val = tuple(val)
            group[val].append(s)

        res = [i for i in group.values()]
        return res