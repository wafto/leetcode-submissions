class Solution:
    def numSquares(self, n: int) -> int:
        squares = [num ** 2 for num in range(1, n + 1) if num ** 2 <= n]

        @cache
        def dp(num: int) -> int:
            if num in squares:
                return 1

            best = n + 1
            
            for square in squares:
                diff = num - square
                
                if diff <= 0:
                    break
                
                best = min(best, dp(diff) + 1)
                
            return best

        return dp(n)


