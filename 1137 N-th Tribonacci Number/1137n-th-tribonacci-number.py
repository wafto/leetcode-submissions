class Solution:
    def tribonacci(self, n: int) -> int:
        
        @cache
        def dp(n: int) -> int:
            if n == 0:
                return 0
            
            if n in [1, 2]:
                return 1
            
            return dp(n - 3) + dp(n - 2) + dp(n - 1)

        return dp(n)