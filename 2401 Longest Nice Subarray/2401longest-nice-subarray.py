class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n, left, longest = len(nums), 0, 0
        mask = 0

        for right in range(n):
            while mask & nums[right]:
                mask = mask ^ nums[left]
                left += 1
            
            longest = max(longest, right - left + 1)
            mask = mask | nums[right]

        return longest    
        