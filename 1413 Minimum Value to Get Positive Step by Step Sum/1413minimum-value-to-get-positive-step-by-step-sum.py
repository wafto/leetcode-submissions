class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        acc, low = 0, 0
        for n in nums:
            acc += n
            low = min(low, acc)
            
        return abs(low) + 1
            