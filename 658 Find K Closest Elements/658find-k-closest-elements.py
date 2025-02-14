class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            distance = abs(num - x)
            heapq.heappush(heap, (-distance, -num))
            if len(heap) > k:
                heapq.heappop(heap)

        return sorted([-p[1] for p in heap])