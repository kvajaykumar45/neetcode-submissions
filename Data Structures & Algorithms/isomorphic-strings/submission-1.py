class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1, m2 = {}, {}
        for i in range(len(s)):
            ch1, ch2 = s[i], t[i]
            if (ch1 in m1 and m1[ch1] != ch2) or (ch2 in m2 and m2[ch2] != ch1):
                return False
            m1[ch1] = ch2
            m2[ch2] = ch1
        return True


        