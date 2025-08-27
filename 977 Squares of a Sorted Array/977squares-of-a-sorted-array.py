class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        left, right, curr = 0, n - 1, n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[curr] = nums[left] ** 2
                left += 1
            else:
                ans[curr] = nums[right] ** 2
                right -= 1
            curr -= 1

        return ans
