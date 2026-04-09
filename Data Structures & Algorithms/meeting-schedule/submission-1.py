"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # check if there are overlaps
        # when you have two intervals A, B, overlaps don't appear when
            # start B is >= end A (B is AFTER A)
            # or 
            # end B is <= start A (B is BEFORE A)
        # if neither condition is met, then A and B are overlapped
        # if meethings are sorted, and we now that B is always after A,
        # then B overlap with A if
         # start B < end A
        # we can find the answer in a linear check
        if not intervals:
            return True
        intervals.sort(key=lambda Interval: Interval.start) # make sure our meetings are sorted by the start time
        prevInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start < prevInterval.end:
                return False
            prevInterval = intervals[i]
        return True
