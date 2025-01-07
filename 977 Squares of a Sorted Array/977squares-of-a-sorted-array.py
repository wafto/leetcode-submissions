class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, index = 0, len(nums) - 1, len(nums) - 1
        output = [0] * len(nums)
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                output[index] = nums[left] ** 2
                left += 1
            else:
                output[index] = nums[right] ** 2
                right -= 1
            index -= 1
            
        return output
        
        
        
        