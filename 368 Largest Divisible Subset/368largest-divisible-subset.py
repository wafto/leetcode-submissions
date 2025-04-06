class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        @cache
        def dp(i: int, prev: int) -> List[int]:
            if i == len(nums):
                return []
            
            res = dp(i + 1, prev)

            if nums[i] % prev == 0:
                tmp = [nums[i]] + dp(i + 1, nums[i])
                res = tmp if len(tmp) > len(res) else res

            return res

        return dp(0, 1)