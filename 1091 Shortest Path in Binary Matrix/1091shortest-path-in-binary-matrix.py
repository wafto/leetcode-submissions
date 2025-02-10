class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        path = 0

        if grid[0][0] == 0:
            queue.append((0, 0))

        while queue:
            path += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return path
                
                neighbors = [
                    (r - 1, c - 1), 
                    (r - 1, c), 
                    (r - 1, c + 1), 
                    (r, c - 1), 
                    (r, c + 1), 
                    (r + 1, c - 1), 
                    (r + 1, c),
                    (r + 1, c + 1),
                ]

                for nr, nc in neighbors:
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    if grid[nr][nc] == 0:
                        queue.append((nr, nc))
                
        return -1

        
                

            