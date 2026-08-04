class MyStack:

    def __init__(self):
        self.stk = []
        self.dummy = []

    def push(self, x: int) -> None:
        if not self.stk:
            self.stk.append(x)
        else:
            while self.stk:
                self.dummy.append(self.stk.pop())
            self.stk.append(x)
            while self.dummy:
                self.stk.append(self.dummy.pop())

    def pop(self) -> int:
        return self.stk.pop(0)
        

    def top(self) -> int:
        return self.stk[0]
        

    def empty(self) -> bool:
        return len(self.stk) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()