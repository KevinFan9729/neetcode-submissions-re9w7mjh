class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        def merge(currInterval, newInterval):
            mergeStart = min (currInterval[0], newInterval[0])
            mergeEnd = max (currInterval[1], newInterval[1])
            return [mergeStart,mergeEnd]

        for i in range(len(intervals)):
            # newInterval[1] < currInterval[0] means new end is < curr start new is BEFORE the curr
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # newInterval[0] > currInterval[1] means new start is > curr end, new is AFTER the curr
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = merge(intervals[i], newInterval)
        
        res.append(newInterval)
        return res

