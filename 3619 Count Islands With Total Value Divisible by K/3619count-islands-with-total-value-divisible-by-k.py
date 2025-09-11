class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def inbounds(r: int, c: int) -> bool:
            return not (r < 0 or c < 0 or r >= rows or c >= cols)

        def bfs(r: int, c: int) -> int:            
            queue = deque([(r, c)])
            total = grid[r][c]
            grid[r][c] = 0

            while queue:
                qr, qc = queue.popleft()
                
                for nr, nc in [(qr - 1, qc), (qr + 1, qc), (qr, qc - 1), (qr, qc + 1)]:
                    if not inbounds(nr, nc) or grid[nr][nc] == 0:
                        continue
                    total += grid[nr][nc]
                    grid[nr][nc] = 0
                    queue.append((nr, nc))

            return total
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    size = bfs(r, c)
                    islands += 1 if size % k == 0 else 0

        return islands



        