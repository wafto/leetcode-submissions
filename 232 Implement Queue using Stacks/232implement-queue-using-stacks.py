class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        tmp = []
        
        while self.stack:
            tmp.append(self.stack.pop())
        
        last = tmp.pop()

        while tmp:
            self.stack.append(tmp.pop())
        
        return last
        
    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return not self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()