class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        i = 0
        result = ""
        status = False
        while i < n-2:
            if num[i] == num[i+1] == num[i+2]:
                result = max(result, num[i:i+3])
            i+=1
        return result