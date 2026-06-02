class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we should sort the intervals
        # [1,3] [1,5] [6,7]
        # an interval is like [start, end]
        # two intervals are like [starta, enda] [startb, endb]
        # to determine if two intervals are overlapping
        # we just need to check if say enda >= startb
        # merging is like
        # taking the min of starts, and taking the max of ends
        # be worry of chain merging, once we know two intervals can be merged
        # we cannot just add the merged intervals to our res
            # instead we need to use this merged interval as reference for the next
        # if two intervals cannot merged, then the previous interval is safe to be added to res
        # Time: O(n log n)
        # Space: O(n) for output

        # current always stores the interval currently being built.
        res = []
        intervals.sort()
        current = intervals[0]
        for nextIndex in range(1, len(intervals)):
            nextItem = intervals[nextIndex]
            overlap = current[1] >= nextItem[0]
            if not overlap:
                res.append(current)
                current = nextItem
            else:
                merged = [min(current[0], nextItem[0]), max(current[1], nextItem[1])]
                current = merged

        res.append(current)
        return res