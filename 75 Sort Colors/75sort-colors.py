class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for color in nums:
            colors[color] += 1

        i, j = 0, 0
        while i < len(nums):
            while j < len(colors) and colors[j] <= 0:
                j += 1
            nums[i] = j
            colors[j] -= 1
            i += 1

