class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()

    def push(self, x: int) -> None:
        self.first.append(x)

    def pop(self) -> int:
        while len(self.first) > 1:
            self.second.append(self.first.popleft())
        tmp = self.first.popleft()
        while self.second:
            self.first.append(self.second.popleft())
        return tmp

    def top(self) -> int:
        return self.first[-1]        

    def empty(self) -> bool:
        return len(self.first) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()