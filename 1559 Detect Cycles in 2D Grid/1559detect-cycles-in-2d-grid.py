class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        seen = set()

        def dfs(r: int, c: int, pr: int, pc: int) -> bool:
            if (r, c) in seen:
                return False

            seen.add((r, c))

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[r][c] != grid[nr][nc] or (nr, nc) == (pr, pc):
                    continue
                if (nr, nc) in seen:
                    return True
                if dfs(nr, nc, r, c):
                    return True
                
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, -1, -1):
                    return True

        return False