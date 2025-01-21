class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros, ones = 0, 0
        idxhashmap = {}
        ans = 0

        for idx, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1

            diff = ones - zeros

            if diff not in idxhashmap:
                idxhashmap[diff] = idx

            if ones == zeros:
                ans = ones + zeros
            else:
                ans = max(ans, idx - idxhashmap[diff])

        return ans
