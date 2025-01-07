class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, prev, mx, zero = 0, 0, 0, 0

        if len(nums) == 1:
            return 1

        for i in range(len(nums)):
            curr += nums[i]
            if nums[i] == 0:
                prev = curr
                curr = 0
                zero = 1
            mx = max(mx, prev + curr + zero)

        return mx