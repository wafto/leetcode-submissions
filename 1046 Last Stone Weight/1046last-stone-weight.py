class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)

        while len(heap) > 1:
            s1, s2 = heappop(heap), heappop(heap)
            sn = s2 - s1

            if sn != 0:
                heappush(heap, -sn)

        return -heap[0] if heap else 0
            
