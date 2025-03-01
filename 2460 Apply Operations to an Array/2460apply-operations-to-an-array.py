class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n, i, j = len(nums), 0, 0
        ans = [0] * n

        while i < n - 1:
            if nums[i] != 0:
                if nums[i] == nums[i + 1]:
                    ans[j] = nums[i] * 2
                    nums[i + 1] = 0
                else:
                    ans[j] = nums[i]
                j+= 1
            i += 1

        if nums[i] != 0:
            ans[j] = nums[i]

        return ans

