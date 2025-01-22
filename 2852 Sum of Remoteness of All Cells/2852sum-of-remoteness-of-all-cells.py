class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        queue = deque()
        groups = []
        gtotal = 0

        for row in range(n):
            for col in range(n):
                
                if grid[row][col] == -1 or (row, col) in visited:
                    continue
                
                queue.append((row, col))
                visited.add((row, col))
                
                total = grid[row][col]
                cells = 1

                while queue:
                    r, c = queue.popleft()
                    neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                    
                    for nr, nc in neighbors:
                        if nr < 0 or nc < 0 or nr == n or nc == n:
                            continue

                        if grid[nr][nc] == -1 or (nr, nc) in visited:
                            continue
                        
                        total += grid[nr][nc]
                        cells += 1
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                
                gtotal += total
                groups.append((total, cells))
            
        ans = 0

        for t, c in groups:
            ans += (gtotal - t) * c

        return ans
    
        




