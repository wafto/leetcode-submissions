class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum, curr = nums[0], 0

        for num in nums:
            curr = curr + num if curr >= 0 else num
            maxsum = max(maxsum, curr)

        return maxsum
            