class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            elif s[i] == '*':
                star.append(i)
            elif s[i] == ')':
                if len(left) > 0:
                    left.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
       
        while len(left) > 0 and len(star) > 0:
            x = left.pop()
            y = star.pop()
            if x > y:
                return False
        if len(left) > 0:
            return False
        else:
            return True
            
        