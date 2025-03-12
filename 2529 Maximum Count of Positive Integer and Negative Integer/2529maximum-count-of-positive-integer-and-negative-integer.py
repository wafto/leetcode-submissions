class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        
        neg = right + 1

        right = n - 1
        
        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > 0:
                right = mid - 1
            else:
                left = mid + 1

        pos = n - left

        return max(neg, pos)





