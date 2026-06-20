class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0
        for i in range(1,n):
            score += abs(ord(s[i]) - ord(s[i-1]))
        return score


        