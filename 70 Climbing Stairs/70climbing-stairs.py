class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 2, 3: 3}

        def dfs(stairs: int) -> int:
            if stairs in memo:
                return memo[stairs]
            
            memo[stairs] = dfs(stairs - 1) + dfs(stairs - 2)

            return memo[stairs]

        return dfs(n)
        