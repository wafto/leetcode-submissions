class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left, res, acc = 0, n + 1, 0

        for right in range(n):
            acc += nums[right]

            while acc >= target:
                res = min(res, right - left + 1)
                acc -= nums[left]
                left += 1

        return 0 if res == n + 1 else res

            
