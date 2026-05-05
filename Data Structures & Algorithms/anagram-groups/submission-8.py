class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            order = [0]*26
            for c in s:
                idx = ord(c) - ord('a')
                order[idx] += 1
            groups[tuple(order)].append(s)
        res = [val for val in groups.values()]
        return res