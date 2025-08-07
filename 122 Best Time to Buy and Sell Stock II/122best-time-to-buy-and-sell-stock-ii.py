class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n, profit = len(prices), 0

        # [1,   2,   3,   4,   5]
        #                i-1   i    
        # profit = 1 + 1 + 1 + 1 = 4 

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
                
        return profit


