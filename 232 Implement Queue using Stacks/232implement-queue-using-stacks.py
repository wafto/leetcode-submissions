class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        while len(self.first) > 1:
            self.second.append(self.first.pop())
        tmp = self.first.pop()
        while self.second:
            self.first.append(self.second.pop())
        return tmp

    def peek(self) -> int:
        return self.first[0]

    def empty(self) -> bool:
        return len(self.first) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()