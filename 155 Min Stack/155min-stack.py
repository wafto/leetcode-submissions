class MinStack:

    def __init__(self):
        self.data = []
        self.mdata = []

    def push(self, val: int) -> None:
        self.data.append(val)
        if self.mdata:
            self.mdata.append(min(self.mdata[-1], val))
        else:
            self.mdata.append(val)

    def pop(self) -> None:
        self.data.pop()
        self.mdata.pop()        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.mdata[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()