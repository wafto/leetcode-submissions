class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [1, 2]

        for i in range(2, n):
            steps = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = steps

        return dp[1]