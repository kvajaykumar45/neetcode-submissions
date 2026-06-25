from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = Counter(s)
        for each in range(len(s)):
            if f[s[each]] == 1:
                return each
        return -1
        