class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1, m2 = {}, {}
        for ch1, ch2 in zip(s,t):
            if (ch1 in m1 and m1[ch1] != ch2) or (ch2 in m2 and m2[ch2] != ch1):
                return False
            m1[ch1] = ch2
            m2[ch2] = ch1
        return True


        