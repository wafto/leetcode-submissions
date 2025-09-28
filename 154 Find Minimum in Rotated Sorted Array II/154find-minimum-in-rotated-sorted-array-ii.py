class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right, ans = 0, n - 1, float('inf')

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                ans = min(ans, nums[mid])
                left, right = left + 1, right -1
                continue
            
            if nums[mid] >= nums[left]:
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                ans = min(ans, nums[mid])
                right = mid - 1

        return ans
