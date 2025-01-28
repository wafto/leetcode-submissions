class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxcatch = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r == rows or c == cols:
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0
            visited.add((r, c))
            acc = grid[r][c]
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                acc += dfs(nr, nc)
            return acc

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r, c) in visited:
                    continue
                maxcatch = max(maxcatch, dfs(r, c))

        return maxcatch