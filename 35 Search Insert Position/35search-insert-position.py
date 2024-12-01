class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start + end) // 2

            if target == nums[middle]:
                return middle

            if target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1

        return start