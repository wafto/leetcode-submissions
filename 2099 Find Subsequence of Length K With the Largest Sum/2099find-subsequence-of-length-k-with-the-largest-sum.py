class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = sorted([(num, i) for i, num in enumerate(nums)])[len(nums) - k:]
        nums.sort(key=lambda t: t[1])

        return [num for num, _ in nums]
        
        