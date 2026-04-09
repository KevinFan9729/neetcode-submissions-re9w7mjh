class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda pair: pair[0]) # sort based on the staring point
        def overlap(intervalA, intervalB):
            # B is after A or B is before A
            if intervalB[0] > intervalA[1] or intervalB[1] < intervalA[0]:
                return False
            return True
        def mergeTwo(intervalA, intervalB):
            mergeStart = min(intervalA[0], intervalB[0])
            mergeEnd = max(intervalA[1], intervalB[1])
            return [mergeStart, mergeEnd]

        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if overlap(res[-1], intervals[i]):
                merged = mergeTwo(res[-1], intervals[i])
                res[-1] = merged
            else:
                res.append(intervals[i])
        return res

        