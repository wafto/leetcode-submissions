class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr, ans, min_prefix, max_prefix = 0, 0, 0, 0

        for num in nums:
            curr += num
            ans = max(ans, abs(curr - max_prefix), abs(curr - min_prefix))
            max_prefix = max(max_prefix, curr)
            min_prefix = min(min_prefix, curr)

        return ans