class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n, ps, ans = len(nums), 0, 0
        indices = {}

        for i in range(n):
            ps += nums[i]

            if ps == k:
                ans = i + 1

            if ps - k in indices:
                ans = max(ans, i - indices[ps - k])

            if ps not in indices:
                indices[ps] = i

        return ans

