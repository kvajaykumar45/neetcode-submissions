class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for each in s:
            result = result ^ ord(each)
        for each in t:
            result = result ^ ord(each)
        return chr(result)
        