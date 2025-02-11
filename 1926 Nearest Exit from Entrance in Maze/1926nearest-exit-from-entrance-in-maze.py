class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])

        queue = deque([(entrance[0], entrance[1], 0)]) # (r, c, steps)
        seen = {(entrance[0], entrance[1])}

        while queue:
            r, c, steps = queue.popleft()

            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and maze[r][c] == '.' and steps > 0:
                return steps

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or (nr, nc) in seen:
                    continue
                
                if maze[nr][nc] == '.':
                    queue.append((nr, nc, steps + 1))
                
                seen.add((nr, nc))

        return -1