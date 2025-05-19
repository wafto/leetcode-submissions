class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        oranges = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    seen.add((r,c))
                    oranges += 1
                elif grid[r][c] == 1:
                    oranges += 1

        if not oranges:
            return 0

        minutes = -1

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if nr < 0 or nc < 0 or nr == rows or nc == cols:
                        continue
                    if (nr, nc) in seen or grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] == 2
                    seen.add((nr, nc))
                    queue.append((nr, nc))
    
            minutes += 1

        return minutes if oranges == len(seen) else -1