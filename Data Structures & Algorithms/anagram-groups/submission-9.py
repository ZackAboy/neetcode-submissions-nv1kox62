class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)
        for s in strs:
            order = [0]*26
            for c in s:
                i = ord("a") - ord(c)
                order[i] += 1
            ana[tuple(order)].append(s)

        return [x for x in ana.values()]