class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxconsecutive = 0
        current = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                current = 0
            maxconsecutive = max(maxconsecutive, current)
            
        return maxconsecutive
            