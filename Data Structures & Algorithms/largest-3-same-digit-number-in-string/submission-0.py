class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        i = 0
        result = ""
        maxi = "000"
        status = False
        while i < n-2:
            if num[i] == num[i+1] == num[i+2]:
                status = True
                if int(num[i:i+3]) > int(maxi):
                    maxi = num[i:i+3]
            i+=1
        if status:
            return maxi
        else:
            return ""
        
            
