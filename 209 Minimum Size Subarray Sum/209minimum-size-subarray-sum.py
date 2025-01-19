class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, total = 0, 0
        minimal = len(nums) + 1

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minimal = min(minimal, right - left + 1)
                total -= nums[left]
                left += 1

        return minimal if minimal <= len(nums) else 0
