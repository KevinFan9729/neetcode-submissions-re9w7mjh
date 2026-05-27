class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # we sort the input first in ascending order
        # how can we merge
        # we can merge if two intervals has overalps
        # how do determine overlaps?
        # [starta, enda], [startb, endb]
        # overalp if say
            # starta < = startb <= enda
            # then we know that a and b are overlapping
        # we need to then figure out how to merge
        # say we want to merge a and b
        # we want to get [startc, endc]
        # startc = min(starta, startb)
        # endc = max(enda, endb)
        # we need to keep track of previous and current interval
        # previous interval can be the previous interval, or the merged interval
        # Time O(nlogn)
        # Space O(n)
        intervals.sort()
        prev = [None , None]
        res = []

        for curr in intervals:
            starta, enda = prev
            startb, endb = curr
            if starta is None:
                # the start of the iteration
                prev = curr
                continue
            # now we want to check for overlaps
            if starta <= startb <= enda:
                # overlap
                # a and b are overlapping
                # we cannot add the merged one to res
                # as this merge interval may merge further!
                # so we can merge curr and prev
                startc = min(starta, startb)
                endc = max(enda, endb)
                merged = [startc,endc]
                prev = merged
            else:
                # no overlap
                # a and b are not overalpping
                # a is safe to add to the res
                # b still have the potential to merge
                res.append(prev)
                prev = curr

        if prev not in res: # last merged item
            res.append(prev)

        return res