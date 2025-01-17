class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r, i = 0, n - 1, n - 1
        output = [0] * n
        
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                output[i] = nums[l] ** 2
                l += 1
            else:
                output[i] = nums[r] ** 2
                r -= 1
            i -= 1
            
        return output
                
        