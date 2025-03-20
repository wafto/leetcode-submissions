class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 2}

        def dp(stair: int) -> int:
            if stair not in memo:
                memo[stair] = dp(stair - 1) + dp(stair - 2)
            
            return memo[stair]
            
        return dp(n)