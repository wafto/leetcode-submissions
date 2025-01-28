class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 1

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()
        
        self.stack.append((self.day, price))
        self.day += 1

        if len(self.stack) == 1:
            return self.stack[0][0]
        
        return self.stack[-1][0] - self.stack[-2][0]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)