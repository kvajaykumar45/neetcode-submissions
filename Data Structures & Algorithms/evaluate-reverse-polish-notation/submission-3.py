class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for i in tokens:
            if i not in "+-*/":
                stk.append(int(i))
            else:
                op2 = stk.pop()
                op1 = stk.pop()
                if i == '+':
                    stk.append(op1 + op2)
                elif i == '-':
                    stk.append(op1 - op2)
                elif i == '*':
                    stk.append(op1 * op2)
                elif i == '/':
                    stk.append(int(op1 / op2))
        return stk[-1]
        
        