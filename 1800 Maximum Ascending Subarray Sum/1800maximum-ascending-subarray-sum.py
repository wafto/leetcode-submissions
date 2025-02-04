class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr_sum, curr_max = nums[0], nums[0] 
    
        for i in range(1, len(nums)):
            curr_sum = curr_sum + nums[i] if nums[i - 1] < nums[i] else nums[i]
            curr_max = max(curr_max, curr_sum)

        return curr_max
