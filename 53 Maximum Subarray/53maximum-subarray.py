class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr, maximum = 0, nums[0]

        for num in nums:
            curr = max(curr, 0) + num
            maximum = max(maximum, curr)

        return maximum