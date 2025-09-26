class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (right + left) // 2

            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return nums[right]
