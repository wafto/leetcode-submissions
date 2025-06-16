class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        low, res = nums[0], -1 

        for i in range(1, len(nums)):
            res = max(res, nums[i] - low)
            low = min(low, nums[i])
            
        return res if res > 0 else -1 