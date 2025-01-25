class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.total = 0
        self.csize = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.csize += 1
        self.total += val

        if self.csize > self.size:
            self.csize -= 1
            self.total -= self.queue.popleft()
        
        return self.total / self.csize


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)