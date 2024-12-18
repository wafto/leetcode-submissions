class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        size = len(prices)
        output = prices.copy()

        for i in range(size - 1):
            j = i + 1
            while j < size and prices[i] < prices[j]:
                j += 1
            if j < size:
                output[i] = output[i] - output[j]
        
        return output


