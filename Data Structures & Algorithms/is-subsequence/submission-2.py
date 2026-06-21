class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n = len(t)
        m = len(s)
        count = 0
        if m==0:
            return True
        while i < n:
            if s[j] == t[i]: 
                j += 1
                count += 1
                if count == m:
                    return True
            i += 1
        return False
