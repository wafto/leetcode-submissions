class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        heap = []

        for r in range(rows):
            heap.append((mat[r].count(1), r))

        heapify(heap)

        ans = []
        for _ in range(k):
            ans.append(heappop(heap)[1])

        return ans