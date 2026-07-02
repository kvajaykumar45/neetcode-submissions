class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        score = 0
        maxi = 0
        for i in range(1,n):
            left = s[0:i]
            right = s[i:]
            score = left.count('0') + right.count('1')
            if score > maxi:
                maxi = score
        return maxi


        