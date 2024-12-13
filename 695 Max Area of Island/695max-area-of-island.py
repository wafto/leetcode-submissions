class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        largest = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            acc = 1
            acc += dfs(r - 1, c)
            acc += dfs(r + 1, c)
            acc += dfs(r, c - 1)
            acc += dfs(r, c + 1)
            return acc

        for i in range(rows):
            for j in range(cols):
                size = dfs(i, j)
                largest = max(largest, size)
        
        return largest

            


