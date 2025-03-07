class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        @cache
        def dp(r: int, c: int) -> int:
            if r == rows or c == cols:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1

            return dp(r + 1, c) + dp(r, c + 1)


        return dp(0, 0)

            