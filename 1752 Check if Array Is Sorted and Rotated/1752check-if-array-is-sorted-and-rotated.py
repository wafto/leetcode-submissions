class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        if n <= 1:
            return True

        i = 1
        while i < n and nums[i - 1] <= nums[i]:
            i += 1

        if i == n:
            return True
        
        if nums[n - 1] > nums[0] :
            return False

        i += 1
        while i < n and nums[i - 1] <= nums[i]:
            i += 1

        return i == n

            