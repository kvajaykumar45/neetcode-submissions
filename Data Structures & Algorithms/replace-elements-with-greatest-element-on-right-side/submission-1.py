class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        n =  len(arr)
        result = [0] * n
        result[-1] = -1
        #result[-2] = arr[-1]
        #result[-3] = result[-2]
        maxi = result[-1]
        for i in range(n-2,-1,-1):
            if arr[i+1] > maxi:
                maxi = arr[i+1]
            result[i] = maxi
        return result 
            

        