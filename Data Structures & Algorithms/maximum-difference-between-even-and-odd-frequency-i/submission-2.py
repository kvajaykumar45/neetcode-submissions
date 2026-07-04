class Solution:
    def maxDifference(self, s: str) -> int:
        f = Counter(s)
        maxodd = 0
        mineven = 100
        for value in f.values():
            if value % 2:
                maxodd = max(value, maxodd)
            else:
                mineven = min(value, mineven)
        return maxodd - mineven