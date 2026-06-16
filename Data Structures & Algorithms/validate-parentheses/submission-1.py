class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for each in s:
            if each in "([{":
                stk.append(each)
            else:
                if len(stk)==0:
                    return False
                if each == ')':
                    if stk.pop() != '(':
                        return False
                elif each == ']':
                    if stk.pop() != '[':
                        return False
                elif each == '}':
                    if stk.pop() != '{':
                        return False
            
        return len(stk) == 0

        