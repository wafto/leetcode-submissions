class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * (n + 1)

        for r in range(m - 1, -1, -1):
            curr = [0] * (n + 1)
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    curr[c] = 1
                else:
                    curr[c] = prev[c] + curr[c + 1]
            prev = curr

        return prev[0]        