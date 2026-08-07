class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        start = 0
        end = 1
        intervals.sort(key=lambda x:x[end]) 
        removed = 0
        prevend = intervals[0][end]
        for i in range(1, len(intervals)):
            currentstart = intervals[i][start]
            if currentstart >= prevend:
                prevend = intervals[i][end]
            else:
                removed += 1
        return removed
           
        