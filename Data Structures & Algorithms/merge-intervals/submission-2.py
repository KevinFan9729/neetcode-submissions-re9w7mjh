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
        res = []
        intervals.sort()
        merged = None
        prevItem = None
        prevIdx = 0
        while prevIdx <= len(intervals) -2:
            if not prevItem:
                prevItem = intervals[prevIdx]
            nextItem = intervals[prevIdx+1]
            overlap = prevItem[1] >= nextItem[0]
            if not overlap:
                res.append(prevItem)
                prevIdx+=1
                prevItem = None
            else:
                merged = [min(prevItem[0], nextItem[0]), max(prevItem[1], nextItem[1])]
                prevIdx += 1
                prevItem = merged
        if merged and merged not in res:
            res.append(merged)
        elif intervals[-1] not in res:
            res.append(intervals[-1])
        return res