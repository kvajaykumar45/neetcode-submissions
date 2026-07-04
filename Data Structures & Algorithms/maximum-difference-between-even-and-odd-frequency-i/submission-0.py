class Solution:
    def maxDifference(self, s: str) -> int:
        f = Counter(s)
        maxodd = 0
        mineven = 100
        for value in f.values():
            if value%2 != 0:
                if value > maxodd:
                    maxodd = value
            else:
                if value < mineven:
                    mineven = value
        return maxodd - mineven
        