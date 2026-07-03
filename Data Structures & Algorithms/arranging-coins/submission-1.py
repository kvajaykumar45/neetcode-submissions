class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 0
        i = 1
        while True:
            if i <= n:
                n = n - i
                rows += 1
                i += 1
            else:
                return rows
        