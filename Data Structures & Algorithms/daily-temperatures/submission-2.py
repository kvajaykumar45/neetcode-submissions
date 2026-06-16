class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        
        result = []
        i = 0
        while i < length:
            j = i + 1
            while j < length:
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    break
                j = j + 1
            if j == length:
                result.append(0)
            i = i + 1
        return result 
        