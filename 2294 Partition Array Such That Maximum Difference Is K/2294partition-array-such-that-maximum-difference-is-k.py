class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, ans = 0, 1

        for right in range(1, len(nums)):
            if nums[right] - nums[left] > k:
                left = right
                ans += 1

        return ans 


