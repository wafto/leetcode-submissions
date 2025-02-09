class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0 
            if grid[r][c] == '0' or grid[r][c] == 'x':
                return 0
            grid[r][c] = 'x'
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                dfs(nr, nc)
            return 1
             
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += dfs(r, c)

        return islands
            


