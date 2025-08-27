class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, longest = 0, 0

        for num in nums:
            if num:
                curr += 1
                longest = curr if curr > longest else longest
            else:
                curr = 0

        return longest