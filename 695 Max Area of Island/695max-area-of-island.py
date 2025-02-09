class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if grid[r][c] != 1:
                return 0
            size = 1
            grid[r][c] = 2
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                size += dfs(nr, nc)
            return size
        
        max_island = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_island = max(max_island, dfs(r, c))
        
        return max_island

