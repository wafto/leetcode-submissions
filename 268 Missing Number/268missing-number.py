class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        existing = set(nums)
        
        for i in range(n + 1):
            if i not in existing:
                return i
            
        return -1
        
        