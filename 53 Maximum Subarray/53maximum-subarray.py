class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        mx = nums[0]
        curr = 0

        for n in nums:
            curr = max(n, n + curr)
            mx = max(mx, curr)

        return mx