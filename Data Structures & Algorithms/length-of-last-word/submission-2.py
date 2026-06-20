class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        for each in s[::-1]:
            if each == " " and n==0:
                continue
            elif each == " ":
                return n
            else:
                n = n+1
        return n
            

        