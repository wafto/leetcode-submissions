class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        for i in range(cols):
            dp[rows - 1][i] = matrix[rows - 1][i]

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 1, -1, -1):

                minimal = dp[r + 1][c]

                if c - 1 >= 0:
                    minimal = min(minimal, dp[r + 1][c - 1])
                if c + 1 < cols:
                    minimal = min(minimal, dp[r + 1][c + 1])

                dp[r][c] = matrix[r][c] + minimal

        return min(dp[0])





