class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0] * 3

        for num in nums:
            bucket[num] += 1

        i = 0
        for n, count in enumerate(bucket):
            for j in range(count):
                nums[i] = n
                i += 1
