class Solution:
    def firstUniqChar(self, s: str) -> int:
        f = [0] * 26
        for each in s:
            f[ord(each) - ord('a')] += 1
        for i,ch in enumerate(s):
            if f[ord(ch) - ord('a')] == 1:
                return i
        return -1