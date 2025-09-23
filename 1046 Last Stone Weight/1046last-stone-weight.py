class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            a, b = heappop(heap), heappop(heap)
            c = b - a
            if c > 0:
                heappush(heap, -c)

        return -heap[0] if heap else 0
        