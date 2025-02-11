class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])

        def manhattan_distance(r: int, c: int) -> int:
            return (rows - 1) - r + (cols - 1) - c

        if k >= manhattan_distance(0, 0):
            return manhattan_distance(0, 0)

        heap = [(manhattan_distance(0, 0), 0, 0, 0, k)]

        visited = set([(0, 0, k)])

        while heap:
            estimation, steps, r, c, remain = heapq.heappop(heap)
            
            #if r == rows - 1 and c == cols - 1:
            #    return steps

            if estimation - steps <= remain:
                return estimation
            
            for nr, nc in [(r + 1, c), (r, c + 1), (r, c - 1), (r - 1, c)]:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc, remain) in visited:
                    continue
            
                if grid[nr][nc] == 0:
                    nestimation = manhattan_distance(nr, nc) + steps + 1
                    heapq.heappush(heap, (nestimation, steps + 1, nr, nc, remain))
                    visited.add((nr, nc, remain))

                elif remain and grid[nr][nc] == 1:
                    nestimation = manhattan_distance(nr, nc) + steps + 1
                    heapq.heappush(heap, (nestimation, steps + 1, nr, nc, remain - 1))
                    visited.add((nr, nc, remain - 1))

        return -1
