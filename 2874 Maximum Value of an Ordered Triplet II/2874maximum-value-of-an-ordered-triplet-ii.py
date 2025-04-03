class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        curr_max, diff_max, ans = nums[0], 0, 0

        for k in range(1, len(nums)):
            ans = max(ans, diff_max * nums[k])
            curr_max = max(curr_max, nums[k])
            diff_max = max(diff_max, curr_max - nums[k])

        return ans