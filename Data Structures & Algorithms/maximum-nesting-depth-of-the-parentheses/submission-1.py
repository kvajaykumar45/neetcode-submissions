class Solution:
    def maxDepth(self, s: str) -> int:
        maxlength = 0
        stk = 0
        for i in s:
            if i == '(':
                stk += 1
                maxlength = max(stk, maxlength)
            elif i == ')':
                stk -= 1
        return maxlength

            
        