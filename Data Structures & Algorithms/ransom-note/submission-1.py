class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for k,v in c1.items():
            if k not in c2:
                return False
            elif c1[k] > c2[k]:
                return False
        return True



        