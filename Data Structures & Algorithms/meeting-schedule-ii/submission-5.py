"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # ok so if two intervals are overallping we need a new room
        # sort based on start time first doing so can help us to check adjcent interval for overalps
        # what is a overalp
        # say we have two intervals
        # [startA, endA] [startB, endB]
        # there is an overlap if
        # startB < endA
        # For meeting rooms, comparing only adjacent intervals is not enough, 
        # because a long earlier meeting can overlap with many later meetings.
        # After sorting by start time, you need to know the earliest ending active meeting, not just the previous interval
        # heap = [end times of active meetings]
        # Time O(nlogn)
        # Space O(n)
        if len(intervals) == 0:
            return 0
        from operator import attrgetter
        intervals.sort(key = attrgetter('start')) # or lambda x : x.start
        heap = [(intervals[0].end)]
        heapq.heapify(heap)
        active = intervals[0]
        numRoom = 1 
        for meetingIdx in range(1, len(intervals)):
            newMeeting = intervals[meetingIdx]
            if heap and heap[0] > newMeeting.start:
                # earlist active meeting's end time is greater than the new meeting's start time
                numRoom += 1 # NEED A NEW ROOM 
                heapq.heappush(heap, (newMeeting.end))
            else:
                heapq.heappop(heap) # in this room, the previous meeting can end
                heapq.heappush(heap, (newMeeting.end))
                
        return numRoom

