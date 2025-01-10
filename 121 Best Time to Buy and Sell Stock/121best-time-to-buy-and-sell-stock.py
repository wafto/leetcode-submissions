class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0

        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i] - minprice)

        return maxprofit