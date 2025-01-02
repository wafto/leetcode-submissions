class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0

        for account in accounts:
            currSum = 0
            for n in account:
                currSum += n
            maxSum = max(maxSum, currSum)

        return maxSum