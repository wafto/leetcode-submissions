class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = 2 * k + 1
        ans = [-1] * n

        if n < window:
            return ans

        curr = sum(nums[:window])
        ans[k] = curr // window

        for i in range(window, n):
            curr += nums[i] - nums[i - window]
            ans[i - k] = curr // window

        return ans