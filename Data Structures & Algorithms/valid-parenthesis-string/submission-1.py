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
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
       
        while left and star:
            x = left.pop()
            y = star.pop()
            if x > y:
                return False
        if left:
            return False
        else:
            return True
            
        