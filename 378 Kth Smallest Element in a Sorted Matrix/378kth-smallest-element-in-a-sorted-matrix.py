class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []

        for r in range(n):
            for c in range(n):
                heappush(heap, -matrix[r][c])
                while len(heap) > k:
                    heappop(heap)

        return -heap[0]