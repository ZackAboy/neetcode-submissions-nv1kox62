class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        count = 0
        res = [intervals[0]]

        for start, end in intervals[1:]:
            prevend = res[-1][1]

            if start < prevend:
                count += 1
            else:
                res.append([start, end])
        return count
