class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for am in range(1, amount + 1):
            for coin in coins:
                remain = am - coin
                if remain < 0:
                    break
                dp[am] = min(dp[am], 1 + dp[remain])

        return dp[amount] if dp[amount] != (amount + 1) else -1
