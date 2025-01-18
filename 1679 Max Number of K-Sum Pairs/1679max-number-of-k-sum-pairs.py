class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        left, right = 0, n - 1
        ans = 0

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                ans += 1
                left += 1
                right -= 1
            elif total > k:
                right -= 1
            else:
                left += 1

        return ans

