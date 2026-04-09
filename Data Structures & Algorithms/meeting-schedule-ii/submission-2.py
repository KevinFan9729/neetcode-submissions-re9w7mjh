"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()

        maxCount = 0
        count = 0

        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                count +=1
                s +=1
            else:
                count -=1
                e +=1
            maxCount = max(maxCount, count)
        return maxCount
            


