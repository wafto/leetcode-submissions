class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)

        if total & 1:
            return False

        @cache
        def dp(i: int, target: int) -> bool:
            if target < 0:
                return False

            if i >= n:
                return target == 0

            return dp(i + 1, target) or dp(i + 1, target - nums[i])

        return dp(0, total // 2)
        