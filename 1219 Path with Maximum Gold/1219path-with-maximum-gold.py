class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def backtracking(r: int, c: int) -> int:
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0

            gold = grid[r][c]
            grid[r][c] = 0
            best = 0
            
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                best = max(best, backtracking(nr, nc))

            grid[r][c] = gold

            return gold + best

        answer = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    answer = max(answer, backtracking(r, c))

        return answer