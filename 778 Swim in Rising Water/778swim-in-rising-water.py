class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n, time = len(grid), 0
        visited = set([(0, 0)]) # (row, col)
        heap = [(grid[0][0], 0, 0)] # (time, row, col)


        while heap:
            t, r, c = heappop(heap)

            time = max(time, t)

            if (r, c) == (n - 1, n - 1):
                return time

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr in [-1, n] or nc in [-1, n] or (nr, nc) in visited:
                    continue

                visited.add((nr, nc))
                heappush(heap, (grid[nr][nc], nr, nc))
        
        return -1



