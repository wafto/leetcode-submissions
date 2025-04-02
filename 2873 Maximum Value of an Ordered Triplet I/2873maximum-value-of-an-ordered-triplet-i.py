class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, left = 0, nums[0]
        
        for j in range(1, n - 1):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j + 1, n):
                res = max(res, (left - nums[j]) * nums[k])

        return res