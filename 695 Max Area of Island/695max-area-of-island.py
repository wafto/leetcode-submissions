class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maximal = 0
        
        def area(r: int, c: int) -> int:
            if grid[r][c] != 1:
                return 0

            total = 1
            grid[r][c] = 2

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue
                total += area(nr, nc)

            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maximal = max(maximal, area(r, c))

        return maximal


        
            