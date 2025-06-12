class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        answer = abs(nums[n - 1] - nums[0])

        for i in range(1, n):
            answer = max(answer, abs(nums[i - 1] - nums[i]))

        return answer
