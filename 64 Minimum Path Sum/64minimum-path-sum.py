class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [[0] * (cols + 1) for _ in range(rows)]
        dp.append([float('inf')] * (cols + 1))
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]

        for r in range(rows - 1, -1, -1):
            dp[r][cols] = float('inf')
            for c in range(cols - 1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    continue
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]
            