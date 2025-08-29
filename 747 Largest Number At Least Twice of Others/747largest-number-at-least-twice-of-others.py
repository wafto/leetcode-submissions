class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        j = 0

        for i, num in enumerate(nums):
            if num > nums[j]:
                j = i

        for i, num in enumerate(nums):
            if i != j and num * 2 > nums[j]:
                return -1

        return j




