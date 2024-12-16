class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        # start or end are blocked
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols -1] == 1:
            return 0

        prev = [0] * cols
        for r in range(rows - 1, -1, -1):
            curr = [0] * cols
            if r == rows - 1:
                curr[cols - 1] = 1
            for c in range(cols - 1, -1, -1):
                if obstacleGrid[r][c] != 1:
                    curr[c] += prev[c]
                    if c != cols - 1:
                        curr[c] += curr[c + 1]
            prev = curr

        return prev[0]

        

        