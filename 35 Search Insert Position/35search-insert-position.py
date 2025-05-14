class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R, M = 0, len(nums) - 1, 0

        #if target < nums[0]:
        #    return 0

        #if target > nums[-1]:
        #    return len(nums)

        while L <= R:
            M = (R + L) // 2

            if nums[M] == target:
                return M

            if nums[M] < target:
                L = M + 1
            else:
                R = M - 1
        
        return L