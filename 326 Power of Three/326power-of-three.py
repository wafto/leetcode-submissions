class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        @cache
        def dp(n: int) -> bool:
            if n < 1:
                return False

            if n == 1:
                return True 
            
            if n % 3 != 0:
                return False
            
            return dp(n // 3)

        return dp(n)
