class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, zeros = 0, 0
        longest = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest - 1
