class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        
        i = 0
        n = len(intervals)
        
        while i<n and intervals[i][0] < newInterval[0]:
            i += 1
        
        intervals.insert(i, newInterval)
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prevend = output[-1][1]
            if start <= prevend:
                output[-1][1] = max(end, prevend)
            else:
                output.append([start, end])

        return output