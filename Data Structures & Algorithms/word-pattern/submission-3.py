class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        n = len(s)
        m = len(pattern)
        if n != m:
            return False
        mapp = {}
        ppam = {}
        for i in range(n):
            if pattern[i] in mapp:
                if mapp[pattern[i]] != s[i]:
                    return False
            else:
                mapp[pattern[i]] = s[i]
        for i in range(n):
            if s[i] in ppam:
                if ppam[s[i]] != pattern[i]:
                    return False
            else:
                ppam[s[i]] = pattern[i]
        return True


        