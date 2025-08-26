class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        maximum = (1 << 32) - 1

        for i, num in enumerate(nums):
            if i != num:
                maximum &= num

        return 0 if maximum == (1 << 32) - 1 else maximum
        
            