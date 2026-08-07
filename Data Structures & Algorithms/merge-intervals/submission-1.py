class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = 0
        end = 1
        result = list()
        intervals.sort()
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if result[-1][end] < intervals[i][start]:
                result.append(intervals[i])
            else:
                result[-1][start] = min(result[-1][start], intervals[i][start])
                result[-1][end] = max(result[-1][end], intervals[i][end])
                
        return result



            