class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        maxCurr, minCurr = 0, 0
        total = 0

        for n in nums:
            maxCurr = max(maxCurr + n, n)
            minCurr = min(minCurr + n, n)
            maxSum = max(maxSum, maxCurr)
            minSum = min(minSum, minCurr)
            total += n

        if maxSum < 0:
            return maxSum
        else:
            return max(maxSum, total - minSum)




