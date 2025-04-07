class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n

        prev = 1
        for i in range(n):
            prefix[i] = prev
            prev *= nums[i]

        prev = 1
        for i in range(n - 1, -1, -1):
            prefix[i] *= prev
            prev *= nums[i]

        return prefix