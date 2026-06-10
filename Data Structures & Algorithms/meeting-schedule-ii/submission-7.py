"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # swapping line algo
        # the number of rooms needed is basically the max active rooms we need
        # active room means overalapping meeting (they happen at the same time thus need extra room)
        # consider start and end as event on a number line(time line)
        # if the meeting start we count +1 if a meeting end we count -1
        # loop through the events in sorted order
        # have a running max to record the max room needed at a time which is the min room requried
        # Time O(nlogn)
        # Space O(n)

        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1
        activeRoom = 0
        roomNeeded = 0
        for meeting in sorted(mp):
            activeRoom += mp[meeting]
            roomNeeded = max(roomNeeded, activeRoom)
        return roomNeeded