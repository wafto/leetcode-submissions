class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.count = 1
        self.added_back = set()

    def popSmallest(self) -> int:
        if not self.heap:
            heapq.heappush(self.heap, self.count)
            self.count += 1

        num = heapq.heappop(self.heap)
        
        if num in self.added_back:
            self.added_back.remove(num)
        
        return num

    def addBack(self, num: int) -> None:
        if num < self.count and num not in self.added_back:
            heapq.heappush(self.heap, num)
            self.added_back.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)