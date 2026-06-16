class MinStack:

    def __init__(self):
        self.stk = [] 
        self.ministk =  []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.ministk:
            self.ministk.append(val)
        else:
            self.ministk.append(min(val, self.ministk[-1]))

    def pop(self) -> None:
        self.stk.pop() 
        self.ministk.pop()       

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.ministk[-1]
        
