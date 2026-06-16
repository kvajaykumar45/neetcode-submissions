class MinStack:

    def __init__(self):
        self.stk = [] 
        self.min =  2^31-1     

    def push(self, val: int) -> None:
        self.stk.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        self.stk.pop()        

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return min(self.stk)
        
