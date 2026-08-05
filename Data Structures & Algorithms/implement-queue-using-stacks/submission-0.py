class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        return self.q1.pop(0)
        
        

    def peek(self) -> int:
        return self.q1[0]
        

    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()