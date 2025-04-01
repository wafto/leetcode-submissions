class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        distances = [[0] * cols for _ in range(rows)]
        buildings = 0

        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            seen = {(r, c)}
            dist = 0

            while queue:
                dist += 1
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if nr < 0 or nc < 0 or nr == rows or nc == cols:
                            continue
                        if (nr, nc) in seen or grid[nr][nc] > 0:
                            continue
                        seen.add((nr, nc))
                        queue.append((nr, nc))
                        distances[nr][nc] += dist
                        grid[nr][nc] -= 1
                         
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    buildings += 1
                    bfs(r, c)

        min_distance = float('inf')
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == -buildings:
                    min_distance = min(min_distance, distances[r][c])

        return -1 if min_distance == float('inf') else min_distance

        
            
        