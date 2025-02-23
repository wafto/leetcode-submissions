class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, prev, zero, maximal = 0, 0, 0, 0

        for num in nums:
            curr += num
            if num == 0:
                zero = 1
                prev = curr
                curr = 0
            maximal = max(maximal, prev + zero + curr)

        return maximal