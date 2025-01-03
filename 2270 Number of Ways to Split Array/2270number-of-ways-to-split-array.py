class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        size = len(nums)

        count = 0
        for i in range(size):
            count += nums[i]
            nums[i] = count

        res = 0
        for i in range(1, size):
            left = nums[i - 1]
            right = count - left
            if left >= right:
                res += 1

        return res


