class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * n

        acc = 0
        for i in range(n):
            acc += nums[i]
            ps[i] += acc

        ans = 0
        for i in range(n - 1):
            if ps[i] >= acc - ps[i]:
                ans += 1

        return ans