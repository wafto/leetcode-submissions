class Solution:
    def fib(self, n: int) -> int:
        
        @cache
        def dp(n: int) -> int:
            if n <= 1:
                return n

            return dp(n - 1) + dp(n - 2)

        return dp(n)