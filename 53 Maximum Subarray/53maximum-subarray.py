class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest, curr = nums[0], 0

        for num in nums:
            curr = max(curr + num, num)
            largest = max(largest, curr)

        return largest