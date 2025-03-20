class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        profit = 0

        for price in prices:
            lowest = min(lowest, price)
            profit = max(profit, price - lowest)

        return profit


        