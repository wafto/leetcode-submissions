class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        labels = 2
        islands = defaultdict(int)

        def in_bounds(r: int, c: int) -> bool:
            return not (r < 0 or c < 0 or r >= n or c >= n)

        def label_bfs(r: int, c: int, label: int) -> int:
            if not in_bounds(r, c) or grid[r][c] != 1:
                return 0

            grid[r][c] = label            
            queue = deque()
            queue.append((r, c))
            size = 1

            while queue:
                r, c = queue.popleft()
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if not in_bounds(nr, nc) or grid[nr][nc] != 1:
                        continue
                    size += 1
                    grid[nr][nc] = label
                    queue.append((nr, nc))
            
            return size

        water_cells = []
        largest_island = 0
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    islands[labels] = label_bfs(r, c, labels)
                    largest_island = max(largest_island, islands[labels])
                    labels += 1
                if grid[r][c] == 0:
                    water_cells.append((r, c))

        for wcell in water_cells:
            r, c = wcell
            visited = set([0])
            size = 1
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if in_bounds(nr, nc) and grid[nr][nc] not in visited:
                    size += islands[grid[nr][nc]]
                    visited.add(grid[nr][nc])
            largest_island = max(largest_island, size)

        return largest_island
