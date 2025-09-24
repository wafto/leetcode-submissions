class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, num)
        heappush(self.minheap, -heappop(self.maxheap))
        while len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (self.minheap[0] - self.maxheap[0]) / -2
        return self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()