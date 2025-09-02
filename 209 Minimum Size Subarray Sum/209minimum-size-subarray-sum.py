class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        acc, left = 0, 0
        shortest = len(nums) + 1

        for right in range(len(nums)):
            acc += nums[right]

            while acc >= target:
                shortest = min(shortest, right - left + 1)
                acc -= nums[left]
                left += 1

        return shortest if shortest != len(nums) + 1 else 0




