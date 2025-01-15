class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ps = [0] * len(nums)
        pr = [0] * len(nums)

        prev = 0
        for i in range(len(nums)):
            prev += nums[i]
            ps[i] = prev

        prev = 0
        for i in range(len(nums) - 1, -1, -1):
            prev += nums[i]
            pr[i] = prev

        for i in range(len(nums)):
            if ps[i] == pr[i]:
                return i

        return -1

            