class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        index = 1
        direction = 0

        while index < len(nums):
            diff = nums[index] - nums[index - 1]
            index += 1
    
            if diff == 0:
                continue

            if direction == 0:
                direction = 1 if diff > 0 else -1
            
            if diff > 0 and direction != 1:
                return False

            if diff < 0 and direction != -1:
                return False

        return True



