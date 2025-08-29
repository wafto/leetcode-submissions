class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc, total = 0, sum(nums)

        for i, num in enumerate(nums):
            if acc == total - acc - num:
                return i
            acc += num
        
        return -1


