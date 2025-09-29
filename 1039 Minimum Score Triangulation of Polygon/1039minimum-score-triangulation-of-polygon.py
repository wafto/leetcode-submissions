class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def dp(i: int, k: int) -> int:
            if k - i < 2:
                return 0
            
            ans = float('inf')

            for j in range(i + 1, k):
                score = values[i] * values[j] * values[k]
                ans = min(ans, score + dp(i, j) + dp(j, k))

            return ans

        return dp(0, len(values) - 1)
        