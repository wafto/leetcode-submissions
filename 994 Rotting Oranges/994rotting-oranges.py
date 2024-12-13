class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        fresh = set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))

        if not fresh:
            return 0
                
        minutes = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for rn, cn in neighbors:
                    rx = r + rn
                    cx = c + cn
                    if rx >= 0 and cx >= 0 and rx < rows and cx < cols and grid[rx][cx] == 1: 
                        queue.append((rx, cx))
                        grid[rx][cx] = 2
                        fresh.remove((rx, cx))
            minutes += 1
        return minutes if not fresh else -1
                
                
