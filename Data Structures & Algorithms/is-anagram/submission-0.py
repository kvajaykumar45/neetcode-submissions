class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        f = {}
        for ch in s:
            if ch not in f:
                f[ch] = 1
            else:
                f[ch] += 1
        for ch in t:
            if ch not in f:
                return False
            f[ch] -= 1
            if f[ch] < 0:
                return False
        return True

        