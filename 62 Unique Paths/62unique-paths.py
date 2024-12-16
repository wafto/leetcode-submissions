class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        memo = [[0] * cols for _ in range(rows)]
        
        def paths(r: int, c: int) -> int:
            if r >= rows or c >= cols:
                return 0
            
            if memo[r][c] != 0:
                return memo[r][c]

            if r == rows - 1 or c == cols - 1:
                memo[r][c] = 1
                return memo[r][c]

            memo[r][c] = paths(r + 1, c) + paths(r, c + 1)
            return memo[r][c]
        
        paths(0, 0)
        return memo[0][0]