class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stk = []
        stk.append(0)
        result = [0] * length
        i = 1
        while i < length:
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev = stk.pop()
                result[prev] = abs(prev-i)
            stk.append(i)
            i = i + 1
        return result


        