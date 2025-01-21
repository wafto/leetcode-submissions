class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ps = [grid[0].copy(), grid[1].copy()]

        for i in range(1, n):
            ps[0][i] = ps[0][i - 1] + ps[0][i]
            ps[1][i] = ps[1][i - 1] + ps[1][i] 

        ans = ps[0][n - 1] + ps[1][n - 1]

        for i in range(n):
            r0 = ps[0][n - 1] - ps[0][i]
            r1 = ps[1][i - 1] if i > 0 else 0

            second = max(r0, r1)
            ans = min(ans, second)

        return ans
