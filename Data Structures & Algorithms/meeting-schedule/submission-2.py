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
        sched = []
        for Interval in intervals:
            sched.append([Interval.start, Interval.end])
        sched.sort(key = lambda x: x[0])
        prevend = sched[0][1]

        for start, end in sched[1:]:
            if start < prevend:
                return False
            prevend = end
        return True