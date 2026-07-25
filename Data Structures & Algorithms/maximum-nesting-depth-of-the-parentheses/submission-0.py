class Solution:
    def maxDepth(self, s: str) -> int:
        maxlength = 0
        stk = []
        for i in s:
            if i == '(':
                stk.append(i)
                l = len(stk)
                maxlength = max(l, maxlength)
            elif i == ')':
                stk.pop()
        return maxlength
            
        