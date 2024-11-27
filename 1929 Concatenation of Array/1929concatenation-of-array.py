class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        size = len(nums)
        ans = [None] * (size * 2)

        for i in range(size):
            ans[i] = nums[i]
            ans[i + size] = nums[i]

        return ans