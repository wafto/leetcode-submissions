class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        @cache
        def dp(day: int, holding: bool) -> int:
            if day == n:
                return 0

            skip = dp(day + 1, holding) # skip
            
            if holding:
                return max(skip, prices[day] - fee + dp(day + 1, False)) # sell
            else:
                return max(skip, -prices[day] + dp(day + 1, True)) # buy

        return dp(0, False)