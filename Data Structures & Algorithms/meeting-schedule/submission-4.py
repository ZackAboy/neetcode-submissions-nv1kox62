"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        inter = [[i.start, i.end] for i in intervals]
        
        inter.sort(key = lambda x: x[0])
        
        prev = [inter[0]]

        for start, end in inter[1:]:
            prevend = prev[-1][1]

            if start < prevend:
                return False
            else:
                prev.append([start, end])

        return True