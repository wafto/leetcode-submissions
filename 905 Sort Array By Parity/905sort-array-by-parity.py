class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        left, right = 0, len(ans) - 1

        for num in nums:
            if num & 1:
                ans[right] = num
                right -= 1
            else:
                ans[left] = num
                left += 1

        return ans
