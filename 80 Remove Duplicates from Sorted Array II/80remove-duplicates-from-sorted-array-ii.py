class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0

        while right < len(nums):
            count = 1
            while right < len(nums) - 1 and nums[right] == nums[right + 1]:
                count += 1
                right += 1

            for _ in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            
            right += 1

        return left
