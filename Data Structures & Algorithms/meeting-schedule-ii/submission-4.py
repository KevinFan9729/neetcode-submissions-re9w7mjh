"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this question is can be thought as how many rooms do you need 
        # at max. (This question assume you only have one meeting room, so need different day)
        # you cannot schedule two meetings that overlap into the same room
        # if that is the case, you need a new room to arrange meetings
        meetings = []
        for interval in intervals:
            meetings.append([interval.start, +1])
            meetings.append([interval.end, -1])
        
        meetings.sort() # stored based on time (early to late)
        print(meetings)
        maxVal = 0
        currCount = 0
        for item in meetings:
            currCount += item[1]
            maxVal = max(maxVal , currCount)

        return maxVal
