class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        output = [1] * size

        prev = 1
        for i in range(size):
            output[i] = prev
            prev *= nums[i]

        prev = 1
        for i in range(size - 1, -1, -1):
            output[i] *= prev
            prev *= nums[i]

        return output