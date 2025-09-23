class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [num for num in nums]
        heapify(self.heap)
        self.cap = k
        while len(self.heap) > self.cap:
            heappop(self.heap)
        
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.cap:
            heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)