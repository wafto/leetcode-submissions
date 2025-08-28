class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        zeros, left, longest = 0, 0, 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zeros += 1
            
            while left < n and zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            longest = max(longest, right - left + 1)


        return longest
        