class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        nums.sort()
        count = 1
        longest = 1

        for i in range(1, len(nums)):
            first, second = nums[i - 1], nums[i]

            if first + 1 == second:
                count += 1
                longest = max(longest, count)
            elif first == second:
                continue
            else:
                count = 1

        return longest
