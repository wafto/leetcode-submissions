class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        min_heap, max_heap = [], []

        for i in range(len(weights) - 1):
            w = weights[i] + weights[i + 1]
            heapq.heappush(min_heap, w)
            heapq.heappush(max_heap, -w)

        ans = 0

        for _ in range(k - 1):
            ans += heapq.heappop(max_heap) + heapq.heappop(min_heap)

        return -ans
