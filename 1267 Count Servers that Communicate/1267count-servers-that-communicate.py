class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cntRow = [0] * rows
        cntCol = [0] * cols

        servers = []
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    servers.append((r, c))
                    cntRow[r] += 1
                    cntCol[c] += 1

        connected = 0

        for r, c in servers:
            if cntRow[r] >= 2 or cntCol[c] >= 2:
                connected += 1

        return connected


