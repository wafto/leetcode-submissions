class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heappush(heap, (sqrt(x * x + y * y), x, y))

        ans = []

        for _ in range(min(k, len(heap))):
            _, x, y = heappop(heap)
            ans.append([x, y])

        return ans

