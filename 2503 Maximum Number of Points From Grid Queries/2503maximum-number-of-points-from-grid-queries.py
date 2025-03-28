class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        queries = sorted([(v, i) for i, v in enumerate(queries)])
        ans = [1] * len(queries)

        heap = [(grid[0][0], 0, 0)] # value, row, col
        seen = set([(0, 0)])
        points = 0

        for limit, index in queries:
            while heap and heap[0][0] < limit:
                _, r, c = heapq.heappop(heap)
                points += 1

                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in seen:
                        continue
                    seen.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
                       
            ans[index] = points

        return ans