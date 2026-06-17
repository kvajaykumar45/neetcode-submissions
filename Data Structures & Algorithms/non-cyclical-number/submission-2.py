class Solution:
    def square(self, n):
        s = 0
        while n!=0:
            r = n%10
            s += r*r
            n //= 10
        return s
    
    def isHappy(self, n: int) -> bool:
        h = set()
        h.add(n)
        while True:
            n = self.square(n)
            if n == 1:
                return True
            if n not in h:
                h.add(n)
            else:
                return False
            
 

        


        