class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        nums = [1 if len(str(n)) % 2 == 0 else 0 for n in nums]
        even = 0
        
        for n in nums:
            even += n
        
        return even