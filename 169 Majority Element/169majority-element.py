class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count <= 0:
                num = nums[i]
            count += 1 if nums[i] == num else -1

        return num