class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr, longest, mode = 1, 1, 0

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i] and mode == 1:
                curr += 1
            elif nums[i - 1] < nums[i] and mode != 1:
                curr = 2
                mode = 1
            elif nums[i - 1] > nums[i] and mode == -1:
                curr += 1
            elif nums[i - 1] > nums[i] and mode != -1:
                curr = 2
                mode = -1
            else:
                curr = 1
                mode = 0
            longest = max(longest, curr)

        return longest