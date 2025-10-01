class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        exchange = numBottles
        total = numBottles

        while exchange // numExchange > 0:
            change = exchange // numExchange
            loose = exchange % numExchange
            total += change
            exchange = change + loose

        return total
