class MyStack:

    def __init__(self):
        self.stk = []
        

    def push(self, x: int) -> None:
        self.stk.insert(0,x)

    def pop(self) -> int:
        return self.stk.pop(0)
        

    def top(self) -> int:
        return self.stk[0]
        

    def empty(self) -> bool:
        if self.stk:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()