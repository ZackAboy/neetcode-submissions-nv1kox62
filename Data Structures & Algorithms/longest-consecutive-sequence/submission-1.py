class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = []
        seen = set()
        for i in nums:
            seen.add(i)

        for i in seen:
            j = i
            count = 1
            while j+1 in seen:
                count += 1
                j += 1
            res.append(count)
        print(res)
        return max(res)